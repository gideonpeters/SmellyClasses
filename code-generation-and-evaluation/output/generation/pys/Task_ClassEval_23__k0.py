class CombinationCalculator:
    def __init__(self, items):
        self.items = items

    @staticmethod
    def count(n, k):
        if k == 0 or k == n:
            return 1
        if k > n:
            return 0
        return CombinationCalculator.count(n-1, k-1) + CombinationCalculator.count(n-1, k)

    @staticmethod
    def count_all(n):
        if n < 0:
            return False
        if n == 0:
            return 0
        return float("inf")

    def select_all(self):
        result = []
        for i in range(1, len(self.items) + 1):
            result.extend(list(itertools.combinations(self.items, i)))
        return result

    def select(self, k):
        return list(itertools.combinations(self.items, k))

    def _select(self, start, temp, index, result):
        if index == len(temp):
            result.append([self.items[i] for i in range(len(temp)) if temp[i] is not None])
            return
        for i in range(start, len(self.items)):
            temp[index] = i
            self._select(i + 1, temp, index + 1, result)
            temp[index] = None
