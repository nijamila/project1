from datetime import date, timedelta, datetime
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard_view(request):
    currency_code = request.GET.get('currency', 'UZS')

    # Hisobot turi va sanalar
    report_type = request.GET.get('report_type', 'all')
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    today = datetime.now().date()
    start_date = end_date = None


    today = date.today()
    if report_type == 'daily':
        start_date = end_date = today
    elif report_type == 'weekly':
        start_date = today - timedelta(days=today.weekday())
        end_date = today
    elif report_type == 'monthly':
        start_date = today.replace(day=1)
        end_date = today
    elif report_type == 'custom' and start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            start_date = end_date = None

    # Walletlar balansi
    from apps.currency.utils import get_conversion_rate
    from apps.wallets.models import Wallet

    wallets = Wallet.objects.filter(user=request.user)
    balance = sum(
        Decimal(w.balance) * Decimal(get_conversion_rate(w.currency.code, currency_code))
        for w in wallets
    )

    # Category summary
    from apps.reports.utils import get_category_summary
    category_data = get_category_summary(request.user, currency_code, start_date, end_date)

    total_income = sum(category_data['income'].values())
    total_expense = sum(category_data['expense'].values())

    chart_income_labels = [k for k in category_data['income'].keys()]
    chart_income_values = [float(v) for v in category_data['income'].values()]

    chart_expense_labels = [k for k in category_data['expense'].keys()]
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
        'end_date': end_date
    })
