class DataStatistics:
    def mean(self, data):
        return round(sum(data) / len(data), 2)

    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]

    def mode(self, data):
        counts = {}
        for num in data:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        max_count = max(counts.values())
        modes = [num for num, count in counts.items() if count == max_count]
        return sorted(modes)
