from django import forms
from .models import ContactUs
from django.forms import ModelForm



class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
