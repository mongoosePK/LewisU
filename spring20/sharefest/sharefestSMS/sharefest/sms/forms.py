from django import forms
import requests, json
from django.forms import ModelForm
from .views import result


class SMSForm(forms.Form):
    #here are the fields we'll be using to query the database 
    # for our contact model objects
    ## TODO ##
    # complete is pantry, #
    isPantry = forms.NullBooleanField(widget=forms.NullBooleanSelect)
    zip_code = forms.CharField(max_length=5, label='Zip', widget=forms.TextInput)
    body = forms.CharField(label='Message Body', widget=forms.Textarea)
    
    
######
# below this we will define a function that will 
# query the contacts table for numbers related to the zipcode
# and filtered by isPantry. These numbers will be passed into 
# result() in sms/views.py
## TODO ##
# declare getNumbers function
# query db
# return a list of phone numbers
# 
def getNumbers(form):

    return