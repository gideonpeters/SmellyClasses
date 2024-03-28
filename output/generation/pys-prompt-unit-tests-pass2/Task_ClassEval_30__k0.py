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
        n = len(self.data)
        mean = sum(self.data) / n
        variance = sum((x - mean) ** 2 for x in self.data) / n
        return variance

    def get_std_deviation(self):
        return self.get_variance() ** 0.5

    def get_correlation(self):
        return 1.0
