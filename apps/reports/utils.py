from decimal import Decimal
from apps.transactions.models import Income, Expense
from apps.wallets.models import Wallet
from apps.currency.models import Currency
from collections import defaultdict
from datetime import date

def get_category_summary(user, currency_code='UZS', start_date: date = None, end_date: date = None):
    """
    Har bir category bo'yicha total income va expense summalarini qaytaradi.
    Valyuta konvert qilinadi.
    start_date va end_date berilsa, shu oraliqda filter qiladi.
    """
    target_currency = Currency.objects.get(code=currency_code)

    # Income category bo'yicha
    income_summary = defaultdict(Decimal)
    incomes = Income.objects.filter(user=user)
    if start_date and end_date:
        incomes = incomes.filter(date__range=[start_date, end_date])
    for inc in incomes:
        rate = inc.wallet.currency.get_rate_to(user, target_currency)
        income_summary[inc.category.name] += Decimal(inc.amount) * Decimal(rate)

    # Expense category bo'yicha
    expense_summary = defaultdict(Decimal)
    expenses = Expense.objects.filter(user=user)
    if start_date and end_date:
        expenses = expenses.filter(date__range=[start_date, end_date])
    for exp in expenses:
        rate = exp.wallet.currency.get_rate_to(user, target_currency)
        expense_summary[exp.category.name] += Decimal(exp.amount) * Decimal(rate)

    return {
        'income': dict(income_summary),
        'expense': dict(expense_summary),
        'currency': currency_code
    }
