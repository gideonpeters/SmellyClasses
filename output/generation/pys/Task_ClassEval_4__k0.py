class AssessmentSystem:
    """
    This is a class as a student assessment system, which supports adding students, adding course scores, calculating GPA,
    and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dict in the assessment system.
        """
        self.students = {}

    def add_student(self, name, grade, major):
        """
        Add a new student into self.students dict
        :param name: str, student name
        :param grade: int, student grade
        :param major: str, student major
        """
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of a specific course for a student in self.students
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        """
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get the average grade of a student.
        :param name: str, student name
        :return: float, average grade of the student if available, otherwise None
        """
        if name in self.students and self.students[name]['courses']:
            scores = self.students[name]['courses'].values()
            return sum(scores) / len(scores)
        return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60.
        :return: list of str, student names
        """
        return [name for name, student in self.students.items() if any(score < 60 for score in student['courses'].values())]

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average score of the course if available, otherwise None
        """
        scores = [student['courses'][course] for student in self.students.values() if course in student['courses'] and student['courses'][course] is not None]
        if scores:
            return sum(scores) / len(scores)
        return None

    def get_top_student(self):
        """
        Calculate every student's GPA and find the student with the highest GPA.
        :return: str, name of the student with the highest GPA
        """
        top_student = None
        top_gpa = 0
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > top_gpa:
                top_gpa = gpa
                top_student = name
        return top_student
```
