class Order:
    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        if not dish:
            return False

        for menu_dish in self.menu:
            if menu_dish["dish"] == dish["dish"]:
                if menu_dish["count"] >= dish["count"]:
                    menu_dish["count"] -= dish["count"]
                    self.selected_dishes.append(dish)
                    return True
                else:
                    return False
        return False

    def calculate_total(self):
        total = 0
        for dish in self.selected_dishes:
            total += dish["price"] * dish["count"]
        return total

    def checkout(self):
        if not self.selected_dishes:
            return False

        total = self.calculate_total()
        for dish in self.selected_dishes:
            for menu_dish in self.menu:
                if menu_dish["dish"] == dish["dish"]:
                    menu_dish["count"] -= dish["count"]
        self.selected_dishes = []
        return total
