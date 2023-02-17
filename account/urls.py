from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('stateconst-json/', views.get_state_const_data, name='stateconst-json'),
    path('register-election/', views.election_register, name='register-election'),
    path('register-candidate/', views.candidate_register, name='register-candidate'),
]