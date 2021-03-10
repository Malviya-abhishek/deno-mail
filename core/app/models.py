from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserKey(models.Model):
    user = User
    key = models.CharField(max_length = 10, unique = True)

class Contact(models.Model):
    key = models.ForeignKey(UserKey, on_delete=models.CASCADE)
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    mail = models.EmailField(max_length = 254, unique = True)
    joinDate = models.DateField(auto_now = True)

    def __str__(self):
        return self.fname + ' ' + self.lname
