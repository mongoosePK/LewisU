from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import datetime
from twilio.rest import Client


@login_required
def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {'today' : today})

#this will return the sign up page view
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

def compose(request):
    account_sid = 'AC14a104141d74e903b309af874c4ff626'
    auth_token = 'bb7db7f8a88d759e5063378e0874f51d'
    client = Client(account_sid, auth_token)
    message_to_broadcast = ("Get that Bread")
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,from_=settings.TWILIO_NUMBER,
            body=message_to_broadcast)
    print(message.sid)
    return render(request, 'compose.html')

def upload(request):
    return render(request, 'upload.html')