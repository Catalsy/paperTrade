from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer, UserSerializer
from paperTrade.models import User, Transaction, Stock

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Buy': 'buy/',
        'Sell': 'sell/',
        'Update Funds': 'update-funds/<int:amount>',
        'Transactions': 'transactions/', 
        'User Details': 'user/' 
    }
    return Response(api_urls)

@api_view(['GET'])
def showTransactions(request):
    # Get all Transaction objects
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def buy(request):
    """ 
    Buying has 3 steps: 
    1. Check if there are enough funds, if so, decrease the funds. 
    2. Log the transaction
    3. Update the amount of stocks the user holds
    """
    # Check if there are enough funds
    user = User.objects.get(username=request.user)
    data = request.data
    tranTotal = data['price'] * data['quantity']

    if user.funds >= tranTotal:
        user.funds = user.funds - tranTotal
        user.save()
    
    else:
        return HttpResponse(status=400)

    # Log transaction
    serializer = TransactionSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

    # Update stock amount 
    symbol = data['stock']
    stock = Stock.objects.get(user=request.user, symbol=symbol)

    if stock:
        stock.quantity = stock.quantity + data['quantity']
        stock.save()

    else:
        stock = Stock(symbol=symbol, quantity=data['quantity'], user=request.user)
        stock.save()

    return Response(serializer.data)

def updateFunds(request, amount):
    user = User.objects.get(username=request.user)
    user.funds = amount
    user.save()

    return HttpResponse(status=204)

@api_view(['POST'])
def sell(request):
    """
    Selling has the following steps:
    1. Increasing the user's funds
    2. Logging the transaction
    3. Update stock quantity
    """
    # Increase funds

    # Log transaction

    # Update stock quantity

    pass

@api_view(['GET'])
def userDetails(request):
    pass