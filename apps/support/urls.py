from django.urls import path
from .views import support_view, support_thankyou

urlpatterns = [
    path('', support_view, name='support'),
    path('thank-you/', support_thankyou, name='support_thankyou'),
    path('my-messages/', support_messages_view, name='support_messages'),
]

