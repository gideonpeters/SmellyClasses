import itertools

class ArrangementCalculator:
    @staticmethod
    def count(n, k):
        return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - k)

    @staticmethod
    def count_all(n):
        return 2 ** n

    def __init__(self, elements):
        self.elements = elements

    def select(self, k):
        return list(itertools.permutations(self.elements, k))

    def select_all(self):
        result = []
        for i in range(1, len(self.elements) + 1):
            result.extend(list(itertools.permutations(self.elements, i)))
        return result

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        return n * ArrangementCalculator.factorial(n - 1)
```
This code defines the `ArrangementCalculator` class with methods to calculate arrangements, count all possible arrangements, select arrangements, select all possible arrangements, and calculate factorial. The methods are implemented to pass the provided unit tes