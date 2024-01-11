from abc import ABC
class Animal(ABC): 
    def move(self): 
        pass  
class Human(Animal): 
    def move(self): 
        print("I can walk and run") 
class Dog(Animal): 
    def move(self): 
        print("I can bark") 
R = Human() 
R.move() 
R = Dog() 
R.move()

