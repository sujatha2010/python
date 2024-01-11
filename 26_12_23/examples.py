   
n = int(input("enter the number of numbers you want to calculate the sum of even numbers"))
sum = 0
for _ in range(n):
    num = int(input("enter the number"))
    if num %2 == 0 :
        sum += num

print("The sum of even numbers is :", sum)    



