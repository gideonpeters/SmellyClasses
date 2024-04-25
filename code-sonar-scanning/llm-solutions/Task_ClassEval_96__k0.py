class WeatherSystem:
    def __init__(self, city):
        self.city = city
        self.temperature = None

    def query(self, weather_list, tmp_units='celsius'):
        if self.city in weather_list:
            if tmp_units == 'celsius':
                return weather_list[self.city]['temperature'], weather_list[self.city]['weather']
            elif tmp_units == 'fahrenheit':
                celsius_temp = weather_list[self.city]['temperature']
                fahrenheit_temp = (celsius_temp * 9/5) + 32
                return fahrenheit_temp, weather_list[self.city]['weather']
        return False

    def set_city(self, new_city):
        self.city = new_city

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9
