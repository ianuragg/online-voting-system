from django.db import models
import uuid
from account.models import User


stateList = (
        ("", "Select..."),("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh", "Arunachal Pradesh"), ("Assam", "Assam"),
        ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Delhi", "Delhi"), ("Goa", "Goa"), 
        ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"),
        ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"),
        ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"),
        ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
        ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"),
        ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"),
        ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
    )

#Election Model
class Election(models.Model):
    election_uid = models.CharField(max_length=36, default=uuid.uuid4)
    election_state = models.CharField(max_length=100, verbose_name="Election State", choices=stateList)
    election_name = models.CharField(max_length=150, verbose_name="Election Name")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.election_state + " - " + self.election_name

#Candidate Model
class Candidate(models.Model):
    candidate_uid = models.CharField(max_length=36, default=uuid.uuid4)
    cand_election = models.ForeignKey(Election, on_delete = models.CASCADE, related_name='cand_election')
    cand_name = models.CharField(max_length=150, verbose_name="Candidate Name")
    cand_email = models.EmailField(unique=True, verbose_name="Candidate Email")
    cand_state = models.CharField(max_length=100, verbose_name="Candidate State", choices=stateList)
    cand_const = models.CharField(max_length=200, verbose_name="Candidate Constituency")
    cand_party = models.CharField(max_length=150, verbose_name="Party Name")
    cand_about = models.TextField(verbose_name="About")
    total_votes = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

#Result Model
class Result(models.Model):
    voter = models.ForeignKey(User, on_delete = models.CASCADE, related_name='voter_result')
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE, related_name='candidate_result')
    election = models.ForeignKey(Election, on_delete = models.CASCADE, related_name='election_result')
    is_voted = models.BooleanField(default=False)
