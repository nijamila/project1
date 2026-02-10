from django.urls import path
from . import views


urlpatterns = [
    path('incomes/', views.income_list_view, name='transaction_income_list'),
    path('incomes/add/', views.income_create_view, name='transaction_income_create'),
    path('expenses/', views.expense_list_view, name='transaction_expense_list'),
    path('expenses/add/', views.expense_create_view, name='transaction_expense_create'),
    path('transfers/', views.transfer_list_view, name='transaction_transfer_list'),
    path('transfers/add/', views.transfer_create_view, name='transaction_transfer_create'),
]
