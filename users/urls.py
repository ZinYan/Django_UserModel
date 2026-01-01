from django.urls import path
from . import views

app_name = "users" #URL namespace를 지정

urlpatterns = [
    path("", views.main, name="main"),
    path("profile/", views.profile, name="profile"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
