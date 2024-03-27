class CombinationCalculator:
    def __init__(self, elements):
        self.elements = elements

    @staticmethod
    def count(n, r):
        if r == 0 or r == n:
            return 1
        r = min(r, n - r)
        numerator = 1
        denominator = 1
        for i in range(r):
            numerator *= n - i
            denominator *= i + 1
        return numerator // denominator

    @staticmethod
    def count_all(n):
        if n < 0:
            return False
        if n == 0:
            return 0
        return float("inf")

    def select_all(self):
        result = []
        for r in range(len(self.elements) + 1):
            result.extend(self._select(0, [None] * r, 0))
        return result

    def select(self, r):
        return self._select(0, [None] * r, 0)

    def _select(self, start, combination, index):
        if index == len(combination):
            return [list(filter(lambda x: x is not None, combination))]
        result = []
        for i in range(start, len(self.elements)):
            combination[index] = self.elements[i]
            result.extend(self._select(i + 1, combination, index + 1))
        return result
`