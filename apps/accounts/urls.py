from django.urls import path
from . import views
from .views import signup_step1, verify_phone_step, signup_step2

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify-phone/', views.verify_phone_view, name='verify_phone'),
    path('signup/', signup_step1, name='signup_step1'),
    path('verify_phone/<int:user_id>/', verify_phone_step, name='verify_phone_step'),
    path('signup/complete/<int:user_id>/', signup_step2, name='signup_step2'),
]

