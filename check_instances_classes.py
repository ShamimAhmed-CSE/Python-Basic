
class Marks:
    pass

class Student:
    pass

st = Student()
m = Marks()

print(isinstance(st, Student))
print(isinstance(m, Marks))

print(issubclass(Student, object))
print(issubclass(Marks, object))