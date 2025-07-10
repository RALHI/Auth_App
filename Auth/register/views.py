from django.views import View 
from django.shortcuts import render
from .form import registerForm

class RegisterView(View):
  def get(self, request):
    form = registerForm
    return render(request, "register/form.html", {"form":form})
  
  def post(self, request):
    pass


# def register(request):
#   return render(request, "register/form.html")
