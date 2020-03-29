from django import forms
import requests, json
from django.forms import ModelForm
class SMSForm(forms.Form):

    isPantry = forms.NullBooleanField(widget=forms.NullBooleanSelect)
    zip_code = forms.CharField(max_length=5, label='Zip', widget=forms.TextInput)
    body = forms.CharField(label='Message Body', widget)