from decimal import Decimal

def get_conversion_rate(from_currency, to_currency):
    rates = {
        ('USD', 'UZS'): 11400,
        ('UZS', 'USD'): 1/11400,
        ('USD', 'EUR'): 0.92,
        ('EUR', 'USD'): 1/0.92,
        ('UZS', 'EUR'): 1 / 11400 * 0.92,
        ('EUR', 'UZS'): 1 / 0.92 * 11400,
        ('USD', 'USD'): 1,
        ('UZS', 'UZS'): 1,
        ('EUR', 'EUR'): 1,
    }
    if from_currency == to_currency:
        return 1
    return rates.get((from_currency, to_currency), 1)
