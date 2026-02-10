from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list_view, name='category_list'),
    path('create/', views.category_create_view, name='category_create'),
    path('<int:pk>/update/', views.category_update_view, name='category_update'),
    path('<int:pk>/delete/', views.category_delete_view, name='category_delete'),
]
