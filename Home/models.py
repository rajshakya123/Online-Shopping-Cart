from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class signUp(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.CharField(max_length=70, default="" )

    def __str__(self):
        return self. first_name
