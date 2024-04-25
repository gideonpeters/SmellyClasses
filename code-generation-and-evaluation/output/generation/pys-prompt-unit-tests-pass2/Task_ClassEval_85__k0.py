class Thermostat:
    def __init__(self, current_temperature, target_temperature, mode):
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self):
        return self.target_temperature

    def set_target_temperature(self, new_target_temperature):
        self.target_temperature = new_target_temperature

    def get_mode(self):
        return self.mode

    def set_mode(self, new_mode):
        if new_mode in ['heat', 'cool']:
            self.mode = new_mode
            return True
        return False

    def auto_set_mode(self):
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        if self.current_temperature < self.target_temperature and self.mode == 'cool':
            self.mode = 'heat'
            return True
        elif self.current_temperature > self.target_temperature and self.mode == 'heat':
            self.mode = 'cool'
            return True
        return False

    def simulate_operation(self):
        if self.mode == 'heat':
            if self.current_temperature < self.target_temperature:
                self.current_temperature += 5
            else:
                self.mode = 'cool'
        elif self.mode == 'cool':
            if self.current_temperature > self.target_temperature:
                self.current_temperature -= 6
            else:
                self.mode = 'heat'
        return abs(self.current_temperature - self.target_temperature)
