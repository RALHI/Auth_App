from django.db import models

class register(models.Model):
  full_name = models.CharField(max_length=100)
  email = models.EmailField()
  user_name = models.CharField(max_length=50)
  password = models.CharField(max_length=128)
  confirm_password = models.CharField(max_length=128)
  
  def __str__(self):
    return f"{self.full_name} - {self.email} - {self.user_name}"
