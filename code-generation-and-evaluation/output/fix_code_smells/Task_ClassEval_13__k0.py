class BookNotFound(Exception):
    pass

class InvalidQuantity(Exception):
    pass

class BookManagement:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title, quantity=1):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity=1):
        if title not in self.inventory:
            raise BookNotFound("Book not found in inventory")
        if self.inventory[title] < quantity:
            raise InvalidQuantity("Invalid quantity to remove")
        self.inventory[title] -= quantity
        if self.inventory[title] == 0:
            del self.inventory[title]

    def view_inventory(self):
        return self.inventory

    def view_book_quantity(self, title):
        return self.inventory.get(title, 0)