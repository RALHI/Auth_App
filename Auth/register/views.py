from django.views import View 
from django.shortcuts import render
from .form import registerForm

class RegisterView(View):
  def get(self, request):
    form = registerForm
    return render(request, "register/form.html", {"form":form})
  
  def post(self, request):
    form = registerForm(request.POST)
    if form.is_valid():
      password = form.cleaned_data.get('password')
      confirm_password = form.cleaned_data.get('confirm_password')
      if password == confirm_password:
        form.save()
        return render(request, "register/form.html", {"form":form, "code": "Successfully Registered"})
      else:
        return render(request, "register/form.html", {"form":form, "code": "Passwords do not match."})
        # form.add_error('confirm_password', 'Passwords do not match.') 
    else:
      return render(request, "register/form.html", {"form":form, "code": "Failed To Register"})


# def register(request):
#   return render(request, "register/form.html")
