class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.77,
            'JPY': 110.47,
            'CAD': 1.31,
            'AUD': 1.37,
            'CNY': 6.46
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            return False
        return amount / self.rates[from_currency] * self.rates[to_currency]

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
