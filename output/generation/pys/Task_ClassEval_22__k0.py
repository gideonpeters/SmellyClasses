class ClassRegistrationSystem:
    def __init__(self):
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        if student not in self.students:
            self.students.append(student)
            return 1
        return 0

    def register_class(self, student_name, class_name):
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        students_by_major = [student["name"] for student in self.students if student["major"] == major]
        return students_by_major

    def get_all_major(self):
        majors = list(set([student["major"] for student in self.students]))
        return majors

    def get_most_popular_class_in_major(self, major):
        classes = [class_name for student, classes in self.students_registration_classes.items() if student["major"] == major for class_name in classes]
        class_count = {}
        for class_name in classes:
            if class_name in class_count:
                class_count[class_name] += 1
            else:
                class_count[class_name] = 1
        most_popular_class = max(class_count, key=class_count.get)
        return most_popular_class
