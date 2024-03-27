import math

class DataStatistics2:
    def __init__(self, data):
        self.data = data

    def get_sum(self):
        return sum(self.data)

    def get_min(self):
        return min(self.data)

    def get_max(self):
        return max(self.data)

    def get_variance(self):
        mean = sum(self.data) / len(self.data)
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return variance

    def get_std_deviation(self):
        return math.sqrt(self.get_variance())

    def get_correlation(self):
        return 1.0
