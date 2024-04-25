class Interpolation:
    def interpolate_1d(self, x_values, y_values, points):
        if not x_values or not y_values or not points:
            return []
        
        result = []
        for point in points:
            if point in x_values:
                result.append(y_values[x_values.index(point)])
            else:
                for i in range(len(x_values) - 1):
                    if x_values[i] <= point <= x_values[i + 1]:
                        slope = (y_values[i + 1] - y_values[i]) / (x_values[i + 1] - x_values[i])
                        interpolated_value = y_values[i] + slope * (point - x_values[i])
                        result.append(interpolated_value)
                        break
        return result

    def interpolate_2d(self, x_values, y_values, z_values, x_points, y_points):
        if not x_values or not y_values or not z_values or not x_points or not y_points:
            return []

        result = []
        for i in range(len(x_points)):
            x_point = x_points[i]
            y_point = y_points[i]
            if x_point in x_values and y_point in y_values:
                x_index = x_values.index(x_point)
                y_index = y_values.index(y_point)
                result.append(z_values[y_index][x_index])
            else:
                for j in range(len(x_values) - 1):
                    if x_values[j] <= x_point <= x_values[j + 1] and y_values[j] <= y_point <= y_values[j + 1]:
                        x_slope = (z_values[j + 1][y_index] - z_values[j][y_index]) / (x_values[j + 1] - x_values[j])
                        y_slope = (z_values[y_index][j + 1] - z_values[y_index][j]) / (y_values[j + 1] - y_values[j])
                        interpolated_value = z_values[j][y_index] + x_slope * (x_point - x_values[j]) + y_slope * (y_point - y_values[y_index])
                        result.append(interpolated_value)
                        break
        return result
`