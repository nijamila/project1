from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from datetime import date, timedelta
from apps.transactions.models import Income, Expense

@login_required
def report_view(request):
    user = request.user
    period = request.GET.get('period')
    currency = request.GET.get('currency', currency_code = 'UZS')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    today = date.today()

    incomes = Income.objects.filter(user=user, wallet__currency=currency)
    expenses = Expense.objects.filter(user=user, wallet__currency=currency)

    if period == 'today':
        incomes = incomes.filter(date=today)
        expenses = expenses.filter(date=today)
    elif period == 'week':
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        incomes = incomes.filter(date__gte=week_start, date__lte=week_end)
        expenses = expenses.filter(date__gte=week_start, date__lte=week_end)
    elif period == 'month':
        incomes = incomes.filter(date__month=today.month, date__year=today.year)
        expenses = expenses.filter(date__month=today.month, date__year=today.year)
    elif period == 'custom' and start_date and end_date:
        incomes = incomes.filter(date__gte=start_date, date__lte=end_date)
        expenses = expenses.filter(date__gte=start_date, date__lte=end_date)

    income_total = incomes.aggregate(total=Sum('amount'))['total'] or 0
    expense_total = expenses.aggregate(total=Sum('amount'))['total'] or 0
    balance = income_total - expense_total

    transactions = sorted(
        list(incomes) + list(expenses),
        key=lambda x: x.date,
        reverse=True
    )

    context = {
        'transactions': transactions,
        'income_total': income_total,
        'expense_total': expense_total,
        'balance': balance,
        'currency': currency,
        'period': period or 'today',
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'reports/report.html', context)
