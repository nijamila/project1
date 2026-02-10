from decimal import Decimal
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext as _

from apps.currency.models import Currency
from apps.reports.utils import get_category_summary
from apps.wallets.models import Wallet
from config.settings import LANGUAGE_CODE


@login_required
def dashboard_view(request):
    currency_code = request.GET.get('currency', 'UZS')
    target_currency = Currency.objects.get(code=currency_code)

    # Hisobot turi va sanalar
    report_type = request.GET.get('report_type', 'all')  # daily, weekly, monthly, custom
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    today = datetime.today().date()
    start_date = end_date = None

    if report_type == 'daily':
        start_date = end_date = today
    elif report_type == 'weekly':
        start_date = today - timedelta(days=today.weekday())  # haftaning boshidan
        end_date = today
    elif report_type == 'monthly':
        start_date = today.replace(day=1)
        end_date = today
    elif report_type == 'custom' and start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            start_date = end_date = None  # noto‘g‘ri formatda bo‘lsa hammasi

    # Walletlar balansi
    wallets = Wallet.objects.filter(user=request.user)
    balance = sum(
        Decimal(w.balance) * Decimal(w.currency.get_rate_to(request.user, target_currency))
        for w in wallets
    )

    # Category summary (date filter qo‘shildi)
    category_data = get_category_summary(request.user, currency_code, start_date, end_date)

    # Umumiy summalar
    total_income = sum(category_data['income'].values())
    total_expense = sum(category_data['expense'].values())

    # Chart uchun labels va values (Decimal -> float)
    chart_income_labels = [_(k) for k in category_data['income'].keys()]
    chart_income_values = [float(v) for v in category_data['income'].values()]

    chart_expense_labels = [_(k) for k in category_data['expense'].keys()]
    chart_expense_values = [float(v) for v in category_data['expense'].values()]

    return render(request, 'dashboard.html', {
        'wallets': wallets,
        'balance': float(balance),
        'total_income': float(total_income),
        'total_expense': float(total_expense),
        'currency': currency_code,
        'chart_income_labels': chart_income_labels,
        'chart_income_values': chart_income_values,
        'chart_expense_labels': chart_expense_labels,
        'chart_expense_values': chart_expense_values,
        'report_type': report_type,
        'start_date': start_date,
        'end_date': end_date,

        'LANGUAGE_CODE': translation.get_language()
    })
