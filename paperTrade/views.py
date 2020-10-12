from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Transaction, Stock

def index(request):
    return render(request,'index.html')