from django.urls import path
from .views import signUp, manage, newsletter, signupForUser

urlpatterns = [
    path('signup/<username>', signUp, name='singUp'),
    path('manage', manage, name='manage'),
    path('newsletter',newsletter, name='newsletter'),
    path('signup-for-user',signupForUser, name='signup-for-user')
]
