from django.urls import path  
from . import views

urlpatterns = [
    path("registration/", views.RegisterView.as_view(), name="RegisterView")
]
