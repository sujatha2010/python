class Animal:
    def speak(self):
        print("Animal speaks")
class Mammal:
    def eat(self):
        print("Mammal eats")

class Dog(Animal, Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  
dog.eat()
dog.bark()  
