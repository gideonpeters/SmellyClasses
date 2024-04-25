class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]["quantity"] += quantity
        else:
            self.items[item_name] = {"price": price, "quantity": quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name]["quantity"] -= quantity
            if self.items[item_name]["quantity"] <= 0:
                del self.items[item_name]

    def view_items(self):
        return self.items

    def total_price(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total
`