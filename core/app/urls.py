from django.urls import path
from .views import signup, manage, newsletter, signupForUser

urlpatterns = [
    path('signup/<username>', signup, name='singup'),
    path('manage', manage, name='manage'),
    path('newsletter',newsletter, name='newsletter'),
    path('signup-for-user',signupForUser, name='signup-for-user'),
]
