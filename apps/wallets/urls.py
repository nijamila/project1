from django.urls import path
from . import views

urlpatterns = [
    path('', views.wallet_list, name='wallet_list'),
    path('create/', views.wallet_create, name='wallet_create'),
    path('<int:pk>/update/', views.wallet_update, name='wallet_update'),
    path('<int:pk>/delete/', views.wallet_delete, name='wallet_delete'),
]
