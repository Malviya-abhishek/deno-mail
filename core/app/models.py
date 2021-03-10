from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length = 10, unique = True)

class Contact(models.Model):
    key = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    mail = models.EmailField(max_length = 254, unique = True)
    joinDate = models.DateField(auto_now = True)

    def __str__(self):
        return self.fname + ' ' + self.lname

class Mail(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length = 100)
    message = models.TextField()
