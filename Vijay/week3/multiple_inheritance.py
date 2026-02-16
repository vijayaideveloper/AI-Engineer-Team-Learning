class MathsTeacher:
    def info1(self):
        print('I Know Maths')

class ScienceTeacher:
    def info12(self):
        print("I Know Science")

class Student(MathsTeacher, ScienceTeacher):
    def info(self):
        self.info1()
        self.info12()
        print("I Know Coding")

s = Student()
s.info()