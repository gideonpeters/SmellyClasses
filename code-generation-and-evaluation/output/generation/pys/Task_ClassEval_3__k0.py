class ArrangementCalculator:
    @staticmethod
    def count(n, k):
        result = 1
        for i in range(n, n-k, -1):
            result *= i
        return result

    @staticmethod
    def count_all(n):
        return 2**n

    def __init__(self, elements):
        self.elements = elements

    def select(self, k):
        from itertools import permutations
        return list(permutations(self.elements, k))

    def select_all(self):
        result = []
        for i in range(1, len(self.elements) + 1):
            result.extend(self.select(i))
        return result

    @staticmethod
    def factorial(n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
