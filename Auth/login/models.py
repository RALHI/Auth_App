from django.db import models

class login(models.Model):
  email = models.EmailField()
  password = models.CharField(max_length=8)
  
  class Meta:
    verbose_name_plural = "Login"
    
  def __str__(self):
    return f"{self.user_name}"
