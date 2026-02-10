from django.urls import path
from . import views

urlpatterns = [
    path('', views.currency_list, name='currency_list'),
    path('add/', views.currency_create, name='currency_create'),
    path('rates/', views.user_currency_rate_list, name='user_currency_rate_list'),
    path('rates/add/', views.user_currency_rate_create, name='user_currency_rate_create'),
]
