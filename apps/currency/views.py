from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Currency, UserCurrencyRate
from .forms import CurrencyForm, UserCurrencyRateForm

@login_required
def currency_list(request):
    currencies = Currency.objects.all()
    return render(request, 'currency/currency_list.html', {'currencies': currencies})

@login_required
def currency_create(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('currency_list')
    else:
        form = CurrencyForm()
    return render(request, 'currency/currency_form.html', {'form': form})

@login_required
def user_currency_rate_list(request):
    rates = UserCurrencyRate.objects.filter(user=request.user)
    return render(request, 'currency/user_currency_rate_list.html', {'rates': rates})

@login_required
def user_currency_rate_create(request):
    if request.method == 'POST':
        form = UserCurrencyRateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.save()
            return redirect('user_currency_rate_list')
    else:
        form = UserCurrencyRateForm()
    return render(request, 'currency/user_currency_rate_form.html', {'form': form})

