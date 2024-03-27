class Order:
    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish_info):
        if not dish_info:
            return False

        dish_name = dish_info["dish"]
        dish_price = dish_info["price"]
        dish_count = dish_info["count"]

        for menu_dish in self.menu:
            if menu_dish["dish"] == dish_name:
                if menu_dish["count"] >= dish_count:
                    menu_dish["count"] -= dish_count
                    self.selected_dishes.append(dish_info)
                    return True
                else:
                    return False
        return False

    def calculate_total(self):
        total = 0
        for dish_info in self.selected_dishes:
            dish_name = dish_info["dish"]
            dish_price = dish_info["price"]
            dish_count = dish_info["count"]
            total += dish_price * dish_count
        return total

    def checkout(self):
        if not self.selected_dishes:
            return False

        total = self.calculate_total()
        for dish_info in self.selected_dishes:
            dish_name = dish_info["dish"]
            for menu_dish in self.menu:
                if menu_dish["dish"] == dish_name:
                    menu_dish["count"] -= dish_info["count"]
        self.selected_dishes = []
        return total
```
This code defines the class `Order` with methods `add_dish`, `calculate_total`, and `checkout` to handle the functionality required by the provided unit tes