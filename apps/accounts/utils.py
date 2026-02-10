import random
from .models import PhoneVerification

def send_phone_code(user):
    code = f"{random.randint(100000, 999999)}"
    PhoneVerification.objects.update_or_create(
        user=user,
        defaults={'code': code, 'verified': False}
    )
    print(f"DEBUG: Code for {user.phone}: {code}")
