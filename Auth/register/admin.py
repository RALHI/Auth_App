from django.contrib import admin
from .models import *

class registerAdmin(admin.ModelAdmin):
  list_display = ('full_name','email','user_name','password')
  search_fields = ('full_name',)
  list_filter = ('email',)
  
admin.site.register(register,registerAdmin)
