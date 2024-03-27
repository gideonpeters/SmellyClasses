class VendingMachine:
    def __init__(self):
        self.inventory = {}
        self.balance = 0.0

    def add_item(self, item_name, price, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        if item_name in self.inventory and self.balance >= self.inventory[item_name]['price'] and self.inventory[item_name]['quantity'] > 0:
            self.balance -= self.inventory[item_name]['price']
            self.inventory[item_name]['quantity'] -= 1
            return 0.0
        else:
            return False

    def restock_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        else:
            return False

    def display_items(self):
        if not self.inventory:
            return False
        items_info = []
        for item, details in self.inventory.items():
            items_info.append(f"{item} - ${details['price']} [{details['quantity']}]")
        return '\n'.join(items_info)
