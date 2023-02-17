from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("elections/", views.current_election, name="elections"),
    path('election/<str:election_idd>/', views.election_detail, name='election'),
    path('candidate/<str:candidate_idd>/', views.candidate, name='candidate'),
    path('voting/<str:election_idd>/', views.voting_process, name='voting'),
    path('election-result/<str:election_idd>/', views.election_result, name='election-result'),
]