class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(self.name , self.age)
class Student(Person):
    pass
x = Student("suji", 26)
x.myfunc()
    

