class PersonRequest:
    def __init__(self, name, sex, phone_number):
        self.name = name if len(name) >= 3 and len(name) <= 20 else None
        self.sex = sex if sex in ['Man', 'Woman'] else None
        self.phone_number = phone_number if len(phone_number) == 11 and phone_number.isdigit() else None