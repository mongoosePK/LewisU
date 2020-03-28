from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {'today' : today })
# Create your views here.
