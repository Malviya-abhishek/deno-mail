from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['fname', 'lname', 'mail']
        lables = { 'fname': 'First Name', 'lname': 'last Name', 'mail':'E-mail' }
