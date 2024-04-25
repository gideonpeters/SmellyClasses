class Statistics3:
    def median(self, data):
        data.sort()
        n = len(data)
        if n % 2 == 0:
            return (data[n//2 - 1] + data[n//2]) / 2
        else:
            return data[n//2]

    def mode(self, data):
        counts = {}
        for num in data:
            counts[num] = counts.get(num, 0) + 1
        max_count = max(counts.values())
        modes = [num for num, count in counts.items() if count == max_count]
        return modes

    def correlation(self, data1, data2):
        if len(data1) != len(data2):
            return None
        mean1 = sum(data1) / len(data1)
        mean2 = sum(data2) / len(data2)
        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
        denominator = (sum((x - mean1) ** 2 for x in data1) * sum((y - mean2) ** 2 for y in data2)) ** 0.5
        if denominator == 0:
            return 1.0
        return numerator / denominator

    def mean(self, data):
        if len(data) == 0:
            return None
        return sum(data) / len(data)

    def correlation_matrix(self, matrix):
        n = len(matrix)
        if n == 0:
            return [[None] * n for _ in range(n)]
        means = [sum(col) / n for col in zip(*matrix)]
        std_devs = [((sum((x - mean) ** 2 for x in col) / n) ** 0.5) if n > 1 else 0 for col, mean in zip(zip(*matrix), means)]
        corr_matrix = [[None if i == j else 1.0 if std_devs[i] == 0 or std_devs[j] == 0 else sum((x - means[i]) * (y - means[j]) for x, y in zip(matrix[i], matrix[j])) / (std_devs[i] * std_devs[j]) for j in range(n)] for i in range(n)]
        return corr_matrix

    def standard_deviation(self, data):
        if len(data) < 2:
            return 0.0
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
        return variance ** 0.5

    def z_score(self, data):
        if len(data) < 2:
            return None
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean) ** 2 for x in data) / (len(data) - 1)) ** 0.5
        return [(x - mean) / std_dev if std_dev != 0 else 0 for x in data]
