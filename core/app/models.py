from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    mail = models.EmailField(max_length = 254, unique = True)
    joinDate = models.DateField(auto_now = True)

    def __str__(self):
        return self.fname + ' ' + self.lname
