class AvgPartition:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def setNum(self):
        avg = len(self.nums) // self.k
        remainder = len(self.nums) % self.k
        return (avg, remainder)

    def get(self, idx):
        avg = len(self.nums) // self.k
        start = idx * avg
        end = start + avg
        if idx == self.k - 1:
            end += len(self.nums) % self.k
        return self.nums[start:end]
