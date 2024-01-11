class Animal:
    def speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barking")
class DogChild(Dog):
    def eat(self):
        print("dog eating")
d = DogChild()
print(isinstance(d,DogChild))
# d.bark()
# d.eat()
# d.speak()


