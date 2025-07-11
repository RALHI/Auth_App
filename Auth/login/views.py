from django.shortcuts import render
# from django.views import View

# class LoginView(View):
#   def get(self, request):
#     pass
  
#   def post(self, request):
#     pass

def LoginView(request):
  return render(request, "login/login.html")
