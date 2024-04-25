class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.47,
            'CAD': 1.25,
            'AUD': 1.30,
            'CNY': 6.40
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        if from_currency not in self.rates or to_currency not in self.rates:
            return False
        return round(amount / self.rates[from_currency] * self.rates[to_currency], 2)

    def get_supported_currencies(self):
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        if currency in self.rates:
            return False
        self.rates[currency] = rate
        return True

    def update_currency_rate(self, currency, rate):
        if currency not in self.rates:
            return False
        self.rates[currency] = rate
        return True
`