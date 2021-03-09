from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm
from .models import Contact

# Create your views here.

app_name = 'app'

def signUp(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contact = Contact.objects.create(fname = data['fname'],lname = data['lname'], mail = data['mail'])
            contact.save()
            return HttpResponse('ThankYou')
    else:
        form = ContactForm()

    ctx = {
        'title':'SignUp',
        'form': form
        }

    return render(request, './app/signup.html'  , ctx )
