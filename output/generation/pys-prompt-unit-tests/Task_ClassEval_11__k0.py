class BitStatusUtil:
    def add(self, num1, num2):
        return num1 | num2

    def has(self, num, check):
        return (num & check) == check

    def remove(self, num, remove):
        return num & ~remove

    def check(self, nums):
        if any(num < 0 for num in nums):
            raise ValueError("Negative numbers not allowed")
        if len(nums) > 3:
            raise ValueError("Exceeded maximum number of elements")
`