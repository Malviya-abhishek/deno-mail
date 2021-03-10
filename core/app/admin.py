from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import Contact, User

admin.site.register(Contact)
admin.site.register(User, UserAdmin)
