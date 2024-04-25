class Statistics3:
    def median(self, nums):
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            return (nums[n//2 - 1] + nums[n//2]) / 2
        else:
            return nums[n//2]

    def mode(self, nums):
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        max_count = max(num_count.values())
        modes = [num for num, count in num_count.items() if count == max_count]
        return modes

    def correlation(self, nums1, nums2):
        if len(nums1) != len(nums2):
            return None
        n = len(nums1)
        sum_xy = sum([x * y for x, y in zip(nums1, nums2)])
        sum_x = sum(nums1)
        sum_y = sum(nums2)
        sum_x_sq = sum([x**2 for x in nums1])
        sum_y_sq = sum([y**2 for y in nums2])
        numerator = n * sum_xy - sum_x * sum_y
        denominator = ((n * sum_x_sq - sum_x**2) * (n * sum_y_sq - sum_y**2)) ** 0.5
        if denominator == 0:
            return 1.0
        return numerator / denominator

    def mean(self, nums):
        if not nums:
            return None
        return sum(nums) / len(nums)

    def correlation_matrix(self, matrix):
        n = len(matrix)
        if n == 0:
            return [[None] * n for _ in range(n)]
        means = [self.mean(col) for col in zip(*matrix)]
        std_devs = [self.standard_deviation(col) for col in zip(*matrix)]
        correlation_matrix = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    correlation_matrix[i][j] = 1.0
                elif std_devs[i] == 0 or std_devs[j] == 0:
                    correlation_matrix[i][j] = None
                else:
                    correlation_matrix[i][j] = self.correlation([row[i] for row in matrix], [row[j] for row in matrix])
        return correlation_matrix

    def standard_deviation(self, nums):
        if len(nums) <= 1:
            return 0.0
        mean = sum(nums) / len(nums)
        variance = sum((x - mean) ** 2 for x in nums) / (len(nums) - 1)
        return variance ** 0.5

    def z_score(self, nums):
        if len(nums) <= 1:
            return None
        mean = self.mean(nums)
        std_dev = self.standard_deviation(nums)
        if std_dev == 0:
            return None
        return [(x - mean) / std_dev for x in nums]
