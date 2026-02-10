from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, PhoneVerificationForm, SignupForm, PhoneForm, PhoneVerificationForm, CompleteSignupForm
from .models import User, PhoneVerification
from .utils import send_phone_code 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if not user.phone_verified:
                return redirect('verify_phone')
            return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def verify_phone_view(request):
    user = request.user
    phone_verif, created = PhoneVerification.objects.get_or_create(user=user)

    send_phone_code(user)

    if request.method == 'POST':
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            input_code = form.cleaned_data['code']
            if phone_verif.code == input_code:
                phone_verif.verified = True
                phone_verif.save()

                user.phone_verified = True
                user.phone_verification_code = phone_verif.code
                user.save()

                print(f"DEBUG: {user.phone} verified!")
                return redirect('dashboard')
            else:
                form.add_error('code', 'Invalid code')
    else:
        form = PhoneVerificationForm()

    return render(request, 'accounts/verify_phone.html', {'form': form})


def signup_step1(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            user, created = User.objects.get_or_create(phone=phone)
            if created:
                user.phone_verified = False
                user.save()
                PhoneVerification.objects.create(user=user)
            return redirect('verify_phone_step', user_id=user.id)
    else:
        form = PhoneForm()
    return render(request, 'accounts/signup_step1.html', {'form': form})

def verify_phone_step(request, user_id):
    user = User.objects.get(id=user_id)
    phone_verif, _ = PhoneVerification.objects.get_or_create(user=user)

    send_phone_code(user)

    if request.method == 'POST':
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['code'] == phone_verif.code:
                phone_verif.verified = True
                phone_verif.save()
                user.phone_verified = True
                user.save()
                return redirect('signup_step2', user_id=user.id)
            else:
                form.add_error('code', 'Invalid code')
    else:
        form = PhoneVerificationForm()
    return render(request, 'accounts/verify_phone.html', {'form': form})

def signup_step2(request, user_id):
    user = User.objects.get(id=user_id)
    if not user.phone_verified:
        return redirect('signup_step1')

    if request.method == 'POST':
        form = CompleteSignupForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CompleteSignupForm(instance=user)

    return render(request, 'accounts/signup_step2.html', {'form': form})
