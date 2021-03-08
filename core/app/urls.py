from django.urls import path
from .views import signUp

urlpatterns = [
    path('', signUp, name='singUp'),
]
