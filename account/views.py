from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from datetime import datetime, date
from account.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
import json
from django.conf import settings
from django.http import JsonResponse
from core.models import Election, Candidate


#Signup View
def register_user(request):
    if request.method == 'POST':
        #Getting form fields
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        dob = request.POST['dob']
        gender = request.POST['gender']
        state = request.POST['state']
        constituency = request.POST['constituency']
        contact = request.POST['contact']

        #Checking User's age
        if len(dob) > 0:
            dob_year = int(dob[0:4])
            dob_month = int(dob[5:7])
            dob_date = int(dob[8:])

            today = date.today()
            age = today.year - dob_year - ((today.month, today.day) < (dob_month, dob_date))

            
        #Check if user exist
        user = User.objects.filter(email=email).exists()

        if user:
            messages.error(request, "Email already exists.")
        elif password1 != password2:
            messages.error(request, "Those passwords didn\'t match. Try again.")
        elif age < 18:
            messages.error(request, "Voter must be 18 years old.")
        else:
            #User Registration
            new_user = User.objects.create_user(password=password1,email=email,fname=fname,lname=lname,dob=dob,gender=gender,state=state,constituency=constituency,contact=contact)
            new_user.save()

            #Authenticating User
            new_user = authenticate(request, email=new_user.email, password=password1)
            if new_user is not None:
                messages.success(request, "Account Created.")
                login(request, new_user)
                return redirect("/")
            else:
                print("user is not authenticated")

    return render(request, "account/register.html")

#Login View
def login_user(request):
    if request.method == "POST":
        #Getting form fields
        email = request.POST['email']
        password = request.POST['password']

        #Authenticating User
        user = authenticate(request, email=email, password = password)
        if user is not None:
            messages.success(request, "Log In Successful")
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Email or Password is Incorrect.")

    return render(request, "account/login.html")

#Logout View
def logout_user(request):
    #Sign out user
    logout(request)
    messages.error(request, "You have successfully logged out!")
    return redirect("login-user")

#Get state and constituency data
def get_state_const_data(request):
    file_path = os.path.join(settings.BASE_DIR, 'static\\file\\data.json')
    with open(file_path, 'r') as file:
        data = json.load(file)

    return JsonResponse({'data':data['stateConst']})


#Election Registration View
@login_required(login_url='login')
def election_register(request):
    # Check if admin
    if request.user.is_admin:
        if request.method == 'POST':
            #Getting form fields
            election_state = request.POST['state']
            election_name = request.POST['election-name']
            start_date = request.POST['start-date']
            end_date = request.POST['end-date']

            #Check if election exist
            election = Election.objects.filter(election_state=election_state, start_date=start_date, end_date=end_date).exists()

            if election:
                messages.error(request, "Election already exists.")
            else:
                #Election Registration
                new_election = Election(election_state=election_state,election_name=election_name, start_date=start_date, end_date=end_date)
                new_election.save()
                messages.success(request, "Election Created.")
    else:
        raise Http404

    return render(request, "account/election_registration.html")

#Candidate Registration View
@login_required(login_url='login')
def candidate_register(request):
    # Check if admin
    if request.user.is_admin:
        if request.method == 'POST':
            #Getting form fields
            election_state = request.POST['state']
            election_name = request.POST['election-name']
            start_date = request.POST['start-date']
            end_date = request.POST['end-date']

            #Check if election exist
            election = Election.objects.filter(election_state=election_state, start_date=start_date, end_date=end_date).exists()

            if election:
                messages.error(request, "Election already exists.")
            else:
                #Election Registration
                new_election = Election(election_state=election_state,election_name=election_name, start_date=start_date, end_date=end_date)
                new_election.save()
                messages.success(request, "Election Created.")
    else:
        raise Http404

    return render(request, "account/candidate_registration.html")
