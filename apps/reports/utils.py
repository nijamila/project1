from decimal import Decimal
from apps.transactions.models import Income, Expense
from collections import defaultdict
from datetime import date
from apps.currency.utils import get_conversion_rate

def get_category_summary(user, currency_code='UZS', start_date: date = None, end_date: date = None):
    income_summary = defaultdict(Decimal)
    incomes = Income.objects.filter(user=user)
    if start_date and end_date:
        incomes = incomes.filter(date__range=[start_date, end_date])
    for inc in incomes:
        rate = get_conversion_rate(inc.wallet.currency.code, currency_code)
        income_summary[inc.category.name] += Decimal(inc.amount) * Decimal(rate)

    expense_summary = defaultdict(Decimal)
    expenses = Expense.objects.filter(user=user)
    if start_date and end_date:
        expenses = expenses.filter(date__range=[start_date, end_date])
    for exp in expenses:
        rate = get_conversion_rate(exp.wallet.currency.code, currency_code)
        expense_summary[exp.category.name] += Decimal(exp.amount) * Decimal(rate)

    return {
        'income': dict(income_summary),
        'expense': dict(expense_summary),
        'currency': currency_code
    }
