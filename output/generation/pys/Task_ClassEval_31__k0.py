import math

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data, list.
        :param data2: The second set of data, list.
        :return: The correlation coefficient, float.
        """
        n = len(data1)
        mean_data1 = sum(data1) / n
        mean_data2 = sum(data2) / n
        cov_xy = sum([(x - mean_data1) * (y - mean_data2) for x, y in zip(data1, data2)])
        var_data1 = sum([(x - mean_data1) ** 2 for x in data1])
        var_data2 = sum([(y - mean_data2) ** 2 for y in data2])
        correlation_coefficient = cov_xy / math.sqrt(var_data1 * var_data2)
        return correlation_coefficient

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        """
        n = len(data)
        mean = sum(data) / n
        variance = sum([(x - mean) ** 2 for x in data]) / n
        skewness = sum([(x - mean) ** 3 for x in data]) / (n * variance ** 1.5)
        return skewness

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        """
        n = len(data)
        mean = sum(data) / n
        variance = sum([(x - mean) ** 2 for x in data]) / n
        kurtosis = sum([(x - mean) ** 4 for x in data]) / (n * variance ** 2) - 3
        return kurtosis

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        """
        pdf_values = [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]
        return pdf_values
