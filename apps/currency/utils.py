def get_conversion_rate(from_currency, to_currency):
    rates = {
        ('USD', 'UZS'): 11400,
        ('UZS', 'USD'): 1/11400,
        ('USD', 'EUR'): 0.92,
        ('EUR', 'USD'): 1/0.92,
        # add more pairs
    }
    if from_currency == to_currency:
        return 1
    return rates.get((from_currency, to_currency), 1) 
