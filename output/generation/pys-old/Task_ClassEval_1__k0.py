    def calculate_circle_area(self):
        """
        calculate the area of circle based on self.radius
        :return: area of circle, float
        """
        return math.pi * self.radius ** 2

    def calculate_sphere_area(self):
        """
        calculate the area of sphere based on self.radius
        :return: area of sphere, float
        """
        return 4 * math.pi * self.radius ** 2

    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :param height: height of cylinder, float
        :return: area of cylinder, float
        """
        return 2 * math.pi * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        """
        calculate the area of sector based on self.radius and angle
        :param angle: angle of sector, float
        :return: area of sector, float
        """
        return 0.5 * self.radius ** 2 * angle

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        calculate the area of annulus based on inner_radius and outer_radius
        :param inner_radius: inner radius of sector, float
        :param outer_radius: outer radius of sector, float
        :return: area of annulus, float
        """
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)
