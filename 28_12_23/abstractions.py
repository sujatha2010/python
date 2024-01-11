# abstract base class work   

from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("the mileage is 30kmph")
class Szuki(Car):
    def mileage(self):
        print("the mielage is 50 kmph")

t = Tesla()
t.mileage()
s = Szuki()
s.mileage()   