from django.urls import path  
from . import views


urlpatterns = [
    # path("login/", views.LoginView.as_view(), name="LoginView"),
    path("login/", views.loginView.as_view(), name="LoginView"),
]
