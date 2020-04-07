from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from twilio.rest import Client
from .forms import SMSForm, getNumbers
from .models import Contact
import datetime

@login_required
def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {'today' : today})

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log user in
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html',{'form':form})

@login_required
def compose(request):
    form = SMSForm()
    context = { 'form': form }


    return render(request, 'compose.html', context=context)

@login_required
def result(request):
    if request.method == 'GET':
        form = SMSForm(request.GET)

        if form.is_valid():
            is_pantry = form.cleaned_data.get('isPantry', '')
            zip_code = form.cleaned_data.get('zip_code', '')
            body = form.cleaned_data.get('body', '')
        ## TODO ##
        # I'd say this is a good place to call the forms.getnumbers()
        # and constrtruct a list out of the returns from the query
        # phone-numbers [list] = forms.getnumbers(form) 
        # for now We'll just use a dummy list of numbers

    ## TODO ##
    ## Hide this acct key stuff in a .env file
    account_sid = 'ACCT_SID_HERE'
    auth_token = 'AUTH_TOKEN_HERE'
    messaging_service_sid = 'MG65a3bf6b7a813d0487eb7c6b69609bbb'
    recipients = ['+18034047382', '+18034047382']
    client = Client(account_sid, auth_token)
    message_to_broadcast = (f'{body}')
    for recipient in recipients:
        if recipient:
            message = client.messages.create(to=recipient,messaging_service_sid=messaging_service_sid,
            body=message_to_broadcast)

    context = {
        'recipient' : recipient,
        'message_body' : message.body,
        'message_sid' : message.sid
    }
    return render(request, 'result.html', context=context)

@login_required
def upload(request):
    return render(request, 'upload.html')
