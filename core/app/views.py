from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import ContactForm, UserRegistrationForm, MailForm
from .models import Contact, User
from django.core.mail import send_mail


def signup(request, username):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get( username = username  )
            contact = Contact.objects.create(key = user  ,fname = data['fname'],lname = data['lname'], mail = data['mail'])
            contact.save()
            return HttpResponse('ThankYou')
    else:
        form = ContactForm()

    ctx = {
        'title':'SignUp',
        'form': form,
        'username':  username,
        }

    return render(request, './app/signup.html'  , ctx )

def signupForUser(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            username = data['username']
            raw_password = data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # user = User.objects.create( first_name = data['first_name'], last_name = data['last_name'], username = data['username'], email = data['email'], password = data['password'])
            # user.save();
            return redirect('/manage')

    else:
        form = UserRegistrationForm()

    ctx = {
        'title':'Registration',
        'form': form
    }

    return render(request, './app/signupForUser.html', ctx)

def manage(request):
    ctx = {
        'title':'Welcome!',
        'content':'this is content'
    }
    return render(request, './app/manage.html'  , ctx )

def newsletter(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            sub = data['subject']
            msg = data['message']
            sender = user.email
            contacts = Contact.objects.filter( key = user )
            recivers = []

            for contact in contacts:
                recivers.append(contact.mail)

            send_mail(sub, msg, sender, recivers, fail_silently=False)
        return HttpResponse('good')


    form = MailForm()

    ctx = {
        'title': 'Newsletter',
        'form': form
    }

    return render(request, './app/newsletter.html', ctx)
