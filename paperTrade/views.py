from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Transaction, Stock

def index(request):
    funds = 0
    investing = 0
    
    try:
        user = request.user
        funds = user.funds
        investing = user.investing
    except:
        pass

    return render(request,'index.html', {
        "funds": funds,
        "investing": investing
    })