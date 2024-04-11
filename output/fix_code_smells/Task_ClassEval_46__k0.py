class Interpolation:
    def interpolate_1d(self, x_values, y_values, points):
        if not x_values or not y_values or not points:
            return []
        
        result = []
        for point in points:
            if point in x_values:
                result.append(y_values[x_values.index(point)])
            else:
                left_x = max([x for x in x_values if x < point])
                right_x = min([x for x in x_values if x > point])
                left_y = y_values[x_values.index(left_x)]
                right_y = y_values[x_values.index(right_x)]
                interpolated_y = left_y + (point - left_x) * (right_y - left_y) / (right_x - left_x)
                result.append(interpolated_y)
        
        return result

    def interpolate_2d(self, x_values, y_values, z_values, x_points, y_points):
        if not x_values or not y_values or not z_values or not x_points or not y_points:
            return []
        
        result = []
        for i in range(len(x_points)):
            x = x_points[i]
            y = y_points[i]
            
            if x in x_values and y in y_values:
                result.append(z_values[x_values.index(x)][y_values.index(y)])
            else:
                left_x = max([x_val for x_val in x_values if x_val < x])
                right_x = min([x_val for x_val in x_values if x_val > x])
                left_y = max([y_val for y_val in y_values if y_val < y])
                right_y = min([y_val for y_val in y_values if y_val > y])
                
                z_left_top = z_values[x_values.index(left_x)][y_values.index(left_y)]
                z_right_top = z_values[x_values.index(right_x)][y_values.index(left_y)]
                z_left_bottom = z_values[x_values.index(left_x)][y_values.index(right_y)]
                z_right_bottom = z_values[x_values.index(right_x)][y_values.index(right_y)]
                
                interpolated_z = (z_left_top * (right_x - x) * (right_y - y) +
                                  z_right_top * (x - left_x) * (right_y - y) +
                                  z_left_bottom * (right_x - x) * (y - left_y) +
                                  z_right_bottom * (x - left_x) * (y - left_y)) / ((right_x - left_x) * (right_y - left_y))
                
                result.append(interpolated_z)
        
        return result