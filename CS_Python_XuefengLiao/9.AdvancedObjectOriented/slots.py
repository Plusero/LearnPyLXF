from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Michael'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(25)


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)


class StudentLim(object):
    __slots__ = ('name', 'age')


s3 = StudentLim()
s.name = 'Bruce'
s.age = 25
# s.score = 99


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 98
print(g.score)
