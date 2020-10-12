from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name="sell"),
    path('stocks/', views.userStocks, name="userStocks"),
    path('update-funds/<int:amount>', views.updateFunds, name="updateFunds"),
    path('update-investing/<int:amount>', views.updateInvesting, name="updateInvesting"),
    path('transactions/', views.showTransactions, name="showTransactions"), 
    path('user/', views.userDetails, name="userDetails")
]