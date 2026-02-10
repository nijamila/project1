from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, Transfer
from .forms import IncomeForm, ExpenseForm, TransferForm
from apps.wallets.models import Wallet
from apps.currency.utils import get_conversion_rate

@login_required
def income_list_view(request):
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transactions/income_list.html', {'incomes': incomes})

@login_required
def expense_list_view(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transactions/expense_list.html', {'expenses': expenses})

@login_required
def transfer_list_view(request):
    transfers = Transfer.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transactions/transfer_list.html', {'transfers': transfers})

@login_required
def income_create_view(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()

            wallet = income.wallet
            wallet.balance += income.amount
            wallet.save()

            return redirect('transaction_income_list')
    else:
        form = IncomeForm(user=request.user)

    return render(request, 'transactions/income_form.html', {'form': form})


def expense_create_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, user=request.user)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.category = form.cleaned_data['category']
            expense.save()

            wallet = expense.wallet

            if hasattr(expense, 'currency') and expense.currency != wallet.currency:
                from apps.currency.utils import get_conversion_rate
                rate = get_conversion_rate(expense.currency.code, wallet.currency.code)
                wallet.balance -= expense.amount * rate
            else:
                wallet.balance -= expense.amount

            wallet.save()

            return redirect('transaction_expense_list')

    else:
        form = ExpenseForm(user=request.user)

    return render(request, 'transactions/expense_form.html', {'form': form})


@login_required
def transfer_create_view(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            transfer = form.save(commit=False)
            transfer.user = request.user
            transfer.save()

            from_wallet = transfer.from_wallet
            to_wallet = transfer.to_wallet
            amount = transfer.amount

            if from_wallet.currency == to_wallet.currency:
                from_wallet.balance -= amount
                to_wallet.balance += amount
            else:
                rate = Decimal(get_conversion_rate(from_wallet.currency.code, to_wallet.currency.code))
                from_wallet.balance -= amount
                to_wallet.balance += amount * rate

            from_wallet.save()
            to_wallet.save()

            return redirect('transaction_transfer_list')
    else:
        form = TransferForm()

    return render(request, 'transactions/transfer_form.html', {'form': form})
