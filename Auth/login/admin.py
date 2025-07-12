from django.contrib import admin
from .models import *

class loginAdmin(admin.ModelAdmin):
  list_display = ('email','password')
  search_fields = ('email',)
  list_filter = ('email',)

admin.site.register(login, loginAdmin)