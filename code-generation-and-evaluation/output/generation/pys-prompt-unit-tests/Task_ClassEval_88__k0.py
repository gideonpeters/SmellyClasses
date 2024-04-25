import math

class TriCalculator:
    def cos(self, angle):
        return round(math.cos(math.radians(angle)), 10)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def taylor(self, angle, terms):
        angle_rad = math.radians(angle)
        result = 0
        for i in range(terms):
            result += ((-1) ** i) * (angle_rad ** (2 * i)) / self.factorial(2 * i)
        return round(result, 10)

    def sin(self, angle):
        return round(math.sin(math.radians(angle)), 10)

    def tan(self, angle):
        if angle % 90 == 0 and angle % 180 != 0:
            return False
        else:
            return round(math.tan(math.radians(angle)), 10)
