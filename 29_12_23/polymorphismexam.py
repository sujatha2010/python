class Cat:
    def sound(self):
        return "Meow"
class Dog:
    def sound(self):
        return "Woof"
def animal_sound(animal):
    return animal.sound()
cat = Cat()
dog = Dog()
print(animal_sound(cat))
print(animal_sound(dog))


   