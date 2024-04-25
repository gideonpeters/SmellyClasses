class TwentyFourPointGame:
    def __init__(self):
        self.nums = []

    def get_my_cards(self):
        import random
        self.nums = random.sample(range(1, 10), 4)
        return self.nums

    def answer(self, expression):
        try:
            result = eval(expression)
            return result == 24
        except:
            return False

    def evaluate_expression(self, expression):
        try:
            eval(expression)
            return True
        except:
            return False
`