from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

app_name = 'app'

def signUp(request):
    ctx = {
        'title':'SignUp',
        'heading':'SignUp'
        }
    return render(request, './app/base.html'  , ctx)
