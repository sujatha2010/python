class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}{self.age}"
        
p1 = Person("jhon", 20)
print(p1)
      