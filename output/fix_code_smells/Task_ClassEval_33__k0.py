class DiscountStrategy:
    fidelity_promo = 'FidelityPromo'
    bulk_item_promo = 'BulkItemPromo'
    large_order_promo = 'LargeOrderPromo'

    def __init__(self, customer, cart, promo=None):
        self.customer = customer
        self.cart = cart
        self.promo = promo

    def total(self):
        total = sum(item['quantity'] * item['price'] for item in self.cart)
        return total

    def due(self):
        total = self.total()
        if self.promo == self.fidelity_promo:
            discount = 0.05 * total if self.customer.get('fidelity', 0) >= 1000 else 0
            total -= discount
        elif self.promo == self.bulk_item_promo:
            discount = 0.1 * total if sum(item['quantity'] for item in self.cart) >= 20 else 0
            total -= discount
        elif self.promo == self.large_order_promo:
            discount = 0.07 * total if len(self.cart) >= 10 else 0
            total -= discount
        return total

    def promotion(self):
        if self.promo == self.fidelity_promo:
            discount = 0.05 * self.total() if self.customer.get('fidelity', 0) >= 1000 else 0
        elif self.promo == self.bulk_item_promo:
            discount = 0.1 * self.total() if sum(item['quantity'] for item in self.cart) >= 20 else 0
        elif self.promo == self.large_order_promo:
            discount = 0.07 * self.total() if len(self.cart) >= 10 else 0
        return discount