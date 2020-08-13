from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('transactions/', views.showTransactions, name='showTransactions'),
    path('buy/', views.buy, name='buy'),
    path('update-funds/<int:amount>', views.updateFunds, name="updateFunds"),

]