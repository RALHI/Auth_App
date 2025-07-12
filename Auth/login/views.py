from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .form import loginForm
from .models import login
from register.models import register
from django.http import HttpResponseRedirect



#this is the function based normal view to render the template
# def LoginView(request):
#   return render(request, "login/login.html")

#this is the class based normal view to render the template
class loginView(View):
  def get(self, request):
    form = loginForm
    return render(request, "login/login.html", {"form":form})
  
  def post(self, request):
    form = loginForm(request.POST)
    if form.is_valid():
      form_email = form.cleaned_data['email']
      form_password = form.cleaned_data['password']
      data = register.objects.filter(email=form_email, password=form_password).first()
      if data:
        data = "Login Successfully"
        return render(request,"login/login.html",{'data': data})
      else:
        print("Not working as expected")

#Template View
# class LoginView(TemplateView):
#   template_name = 'login/login.html'
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
    
    

