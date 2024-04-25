import math

class AreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return round(math.pi * self.radius ** 2, 2)

    def calculate_sphere_area(self):
        return round(4 * math.pi * self.radius ** 2, 2)

    def calculate_cylinder_area(self, height):
        return round(2 * math.pi * self.radius * (self.radius + height), 2)

    def calculate_sector_area(self, angle):
        return round(0.5 * self.radius ** 2 * angle, 2)

    def calculate_annulus_area(self, inner_radius, outer_radius):
        return round(math.pi * (outer_radius ** 2 - inner_radius ** 2), 3)
