from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer, UserSerializer
from paperTrade.models import User, Transaction

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Buy': 'stock-buy/',
        'Sell': 'stock-sell/',
        'Update Funds': 'update-funds/',
        'Transactions': 'transactions/'
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
    serializer = TransactionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

def updateFunds(request, amount):
    user = User.objects.get(username=request.user)
    user.funds = amount
    user.save()

    return HttpResponse(status=204)
