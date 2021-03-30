class student:
    def a(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class CodingBootcamp:
    def __init__(self, course_name, max_students, instructor):
        self.course_name = course_name
        self.max_students = max_students
        self.instructor = instructor
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def display_students(self):
        for student in self.students:
            print(student)

student1 = Student("ziggy Marley", 42, 95)

course1.display_students()