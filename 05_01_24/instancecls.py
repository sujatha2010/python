class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says Woof!")

dog1 = Dog("puppy", 3)
dog2 = Dog("tommy", 5)
print(dog1.name + " is " + str(dog1.age) + " years old.")
dog1.bark()
print(dog2.name + " is " + str(dog2.age) + " years old.")
dog2.bark()
