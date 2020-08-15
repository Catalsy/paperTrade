from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name="sell"),
    path('update-funds/<int:amount>', views.updateFunds, name="updateFunds"),
    path('transactions/', views.showTransactions, name="showTransactions"), 
    path('user/', views.userDetails, name="userDetails")


]