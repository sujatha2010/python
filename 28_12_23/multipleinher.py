class calculation:
    def summation(self,a,b):
        return a+b
class calculation2:
    def Multiplication(self,a,b):
        return a*b
class Derived(calculation, calculation2):
    def divide(self,a,b):
        return a/b
d = Derived()  
print(d.summation(10,20))  
print(d.Multiplication(10,20))  
print(d.divide(10,20))  
