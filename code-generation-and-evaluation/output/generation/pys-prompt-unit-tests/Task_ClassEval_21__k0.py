from datetime import datetime

class Classroom:
    def __init__(self, classroom_id):
        self.classroom_id = classroom_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        check_time = datetime.strptime(check_time, '%H:%M')
        for course in self.courses:
            start_time = datetime.strptime(course['start_time'], '%H:%M')
            end_time = datetime.strptime(course['end_time'], '%H:%M')
            if start_time <= check_time < end_time:
                return False
        return True

    def check_course_conflict(self, new_course):
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M')
        for course in self.courses:
            existing_start_time = datetime.strptime(course['start_time'], '%H:%M')
            existing_end_time = datetime.strptime(course['end_time'], '%H:%M')
            if (new_start_time < existing_end_time and new_end_time > existing_start_time) or (existing_start_time < new_end_time and existing_end_time > new_start_time):
                return True
        return False
