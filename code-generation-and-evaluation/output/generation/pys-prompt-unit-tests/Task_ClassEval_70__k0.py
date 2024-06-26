class PersonRequest:
    def __init__(self, name, sex, phoneNumber):
        self.name = name if len(name) >= 3 and len(name) <= 20 else None
        self.sex = sex if sex in ['Man', 'Woman'] else None
        self.phoneNumber = phoneNumber if phoneNumber.isdigit() and len(phoneNumber) == 11 else None
