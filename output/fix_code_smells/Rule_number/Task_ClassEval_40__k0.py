class FitnessTracker:
    def __init__(self, height, weight, age, gender):
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender

    def get_BMI(self):
        return round(self.weight / (self.height ** 2), 2)

    def condition_judge(self):
        bmi = self.get_BMI()
        if self.gender == "male":
            if bmi < 18.5:
                return -1
            elif 18.5 <= bmi < 25:
                return 0
            else:
                return 1
        else:
            if bmi < 18.5:
                return -1
            elif 18.5 <= bmi < 24:
                return 0
            else:
                return 1

    def calculate_calorie_intake(self):
        if self.gender == "male":
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height * 100) - (5.677 * self.age)
        else:
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height * 100) - (4.330 * self.age)
        
        return round(bmr * 1.2, 2)