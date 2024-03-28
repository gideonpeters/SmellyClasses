class BitStatusUtil:
    def add(self, num1, num2):
        return num1 | num2

    def has(self, num, check):
        return (num & check) == check

    def remove(self, num, remove):
        return num & ~remove

    def check(self, nums):
        for num in nums:
            if num < 0:
                raise ValueError("Negative number not allowed")
            if num < 1 or num > 7:
                raise ValueError("Number out of range")

if __name__ == '__main__':
    unittest.main()
