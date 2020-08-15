from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer, UserSerializer, StockSerializer
from paperTrade.models import User, Transaction, Stock
from django.contrib.auth.decorators import login_required

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Buy': 'buy/',
        'Sell': 'sell/',
        'Stocks': 'stocks/',
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

@login_required
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
        return Response({"error": "not enough funds"})

    # Log transaction
    serializer = TransactionSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

    # Update stock amount 
    symbol = data['stock']
    try :
        stock = Stock.objects.get(user=request.user, symbol=symbol)
        stock.quantity = stock.quantity + data['quantity']
        stock.save()

    except:
        stock = Stock(symbol=symbol, quantity=data['quantity'], user=request.user)
        stock.save()

    return Response(serializer.data)

@login_required
@api_view(['GET'])
def updateFunds(request, amount):
    # Updates funds and returns a response with the updated user data

    user = User.objects.get(username=request.user)
    user.funds = amount
    user.save()

    return Response(extractUserData(request))

@login_required
@api_view(['POST'])
def sell(request):
    """
    Selling has the following steps:
    1. Check if the user has enough stocks and update
    2. Increasing the user's funds
    3. Logging the transaction
    """

    # Check if the user has enough stocks, if so, update quantity
    data = request.data
    try: 
        stock = Stock.objects.get(symbol=data['stock'], user=request.user)
        if stock.quantity >= data['quantity']:
            stock.quantity = stock.quantity - data['quantity']
            stock.save()
    except:
        return Response({"error": "not enough stocks"})

    # Update funds
    user = User.objects.get(username=request.user)
    tranTotal = data['price'] * data['quantity']

    user.funds = user.funds + tranTotal
    user.save()

    # Log transaction
    serializer = TransactionSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@login_required
@api_view(['GET'])
def userDetails(request):
    return Response(extractUserData(request))

@login_required
@api_view(['GET'])
def userStocks(request):
    # Return stocks owned by the current user
    user = User.objects.get(username=request.user)
    stocks = Stock.objects.filter(user=user)
    serializer = StockSerializer(stocks, many=True)

    return Response(serializer.data)

######## HELPER METHODS ########

def extractUserData(request):
    # Return details of the current loged in user
    user = User.objects.get(username=request.user)
    details = {
        "username": user.username,
        "funds": user.funds,
        "investing": user.investing
    }

    return details