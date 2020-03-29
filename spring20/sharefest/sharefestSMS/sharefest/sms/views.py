from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
import datetime
from twilio.rest import Client


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
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html',{'form':form})

@login_required
def compose(request):
    


    return render(request, 'compose.html', context=context)

@login_required
def send_message(request):
    #for recipients we will build a list here using form data to query
    #our db of cliends and create a list for twilio to iterate through
    account_sid = 'AC14a104141d74e903b309af874c4ff626'
    auth_token = '89214aebacde803fada05b92165fff4c'
    messaging_service_sid = 'MG65a3bf6b7a813d0487eb7c6b69609bbb'
    recipients = ['+18034047382']
    client = Client(account_sid, auth_token)
    message_to_broadcast = ("Get that Bread")
    for recipient in recipients:
        if recipient:
            message = client.messages.create(to=recipient,messaging_service_sid=messaging_service_sid,
            body=message_to_broadcast)

    context = {
        'recipient' : recipient,
        'message_body' : message.body,
        'message_sid' : message.sid
    }
    return render(request, 'message_result.html', context=context)

@login_required
def upload(request):
    return render(request, 'upload.html')