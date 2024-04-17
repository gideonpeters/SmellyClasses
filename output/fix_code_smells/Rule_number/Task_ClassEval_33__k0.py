class DiscountStrategy:
    FidelityPromo = 'FidelityPromo'
    BulkItemPromo = 'BulkItemPromo'
    LargeOrderPromo = 'LargeOrderPromo'

    def __init__(self, customer, cart, promo=None):
        self.customer = customer
        self.cart = cart
        self.promo = promo

    def total(self):
        total = sum(item['quantity'] * item['price'] for item in self.cart)
        return total

    def due(self):
        total = self.total()
        discount = 0
        if self.promo == self.FidelityPromo:
            discount = 0.05 * total if self.customer.get('fidelity', 0) >= 1000 else 0
        elif self.promo == self.BulkItemPromo:
            discount = 0.1 * total if sum(item['quantity'] for item in self.cart) >= 20 else 0
        elif self.promo == self.LargeOrderPromo:
            discount = 0.07 * total if len(self.cart) >= 10 else 0
        total -= discount
        return total

    def promotion(self):
        discount = 0
        if self.promo == self.FidelityPromo:
            discount = 0.05 * self.total() if self.customer.get('fidelity', 0) >= 1000 else 0
        elif self.promo == self.BulkItemPromo:
            discount = 0.1 * self.total() if sum(item['quantity'] for item in self.cart) >= 20 else 0
        elif self.promo == self.LargeOrderPromo:
            discount = 0.07 * self.total() if len(self.cart) >= 10 else 0
        return discount