class Course:
    def __init__(self, name, duration, topics):
        self.name = name
        self.duration = duration
        self.topics = []

    def __str__(self):
        return f'Курс: {self.name}, длительность: {self.duration}, тем: {len(self.topics)}'

    def __repr__(self):
        return f'__repr__ {self.name} {self.duration} {self.topics}'

    def add_topic(self, topic: str):
        self.topics.append(topic)

class Instructor:
    def __init__(self, name, surname, seniority, course_list):
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.course_list = []

    def __repr__(self):
        return f'__repr__ {self.name} {self.surname} {self.seniority} {self.course_list}'

    def assign_course(self, course: Course):
        self.course_list.append(course)

    def list_courses(self):
        for course in self.course_list:
            print(course)

class Student:
    def __init__(self, name, surname, age, grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = {}

    def __str__(self):
        return f'Студент: {self.name} {self.surname},возраст:  {self.age}'

    def __repr__(self):
        return f'__repr__ {self.name} {self.surname} {self.age} {self.grade}'

    def enroll(self, course: Course):
        self.grade[course.name] = []

    def add_grade(self, course_name: str, grade: float):
        self.grade[course_name].append(grade)

class TrainingCenter:
    def __init__(self, name, instructor_list, student_list):
        self.name = name
        self.instructor_list = []
        self.student_list = []

    def __repr__(self):
        return f'__repr__ {self.name} {self.instructor_list} {self.student_list}'

    def add_instructor(self, instructor: Instructor):
        self.instructor_list.append(instructor)

    def add_student(self, student: Student):
        self.student_list.append(student)