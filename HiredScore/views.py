from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, timedelta,datetime

def home(request):

   

    return render(request, 'home.html')

