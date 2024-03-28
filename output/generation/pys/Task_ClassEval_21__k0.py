class Classroom:
    def __init__(self, classroom_id):
        self.classroom_id = classroom_id
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        for course in self.courses:
            if course['start_time'] <= check_time < course['end_time']:
                return False
        return True

    def check_course_conflict(self, new_course):
        for course in self.courses:
            if (course['start_time'] < new_course['end_time'] and new_course['start_time'] < course['end_time']):
                return True
        return False
