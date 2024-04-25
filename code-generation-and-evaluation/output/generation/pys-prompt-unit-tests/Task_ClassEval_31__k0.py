import math

class DataStatistics4:
    @staticmethod
    def correlation_coefficient(data1, data2):
        n = len(data1)
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n
        cov = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / n
        std_dev1 = math.sqrt(sum((x - mean1) ** 2 for x in data1) / n)
        std_dev2 = math.sqrt(sum((x - mean2) ** 2 for x in data2) / n)
        return cov / (std_dev1 * std_dev2)

    @staticmethod
    def skewness(data):
        n = len(data)
        mean = sum(data) / n
        std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / n)
        skew = sum((x - mean) ** 3 for x in data) * n / ((n - 1) * (n - 2) * std_dev ** 3)
        return skew

    @staticmethod
    def kurtosis(data):
        n = len(data)
        mean = sum(data) / n
        std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / n)
        kurt = sum((x - mean) ** 4 for x in data) * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * std_dev ** 4) - 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
        return kurt

    @staticmethod
    def pdf(data, mean, std_dev):
        pdf_values = [1 / (std_dev * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mean) / std_dev) ** 2) for x in data]
        return pdf_values
