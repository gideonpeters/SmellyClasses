class AssessmentSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade, major):
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, student_name, course_name, score):
        if student_name in self.students:
            self.students[student_name]['courses'][course_name] = score

    def get_gpa(self, student_name):
        if student_name in self.students:
            scores = self.students[student_name]['courses'].values()
            if scores:
                return sum(scores) / len(scores)
        return None

    def get_all_students_with_fail_course(self):
        fail_students = []
        for student, courses in self.students.items():
            if any(score < 60 for score in courses['courses'].values()):
                fail_students.append(student)
        return fail_students

    def get_course_average(self, course_name):
        scores = [courses['courses'][course_name] for courses in self.students.values() if course_name in courses['courses'] and courses['courses'][course_name] is not None]
        if scores:
            return sum(scores) / len(scores)
        return None

    def get_top_student(self):
        if not self.students:
            return None
        top_student = max(self.students, key=lambda x: sum(self.students[x]['courses'].values(), default=0))
        return top_student
