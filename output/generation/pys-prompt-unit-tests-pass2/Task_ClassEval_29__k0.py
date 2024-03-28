class DataStatistics:
    def mean(self, data):
        return round(sum(data) / len(data), 2)

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
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        max_count = max(counts.values())
        modes = [num for num, count in counts.items() if count == max_count]
        return modes
