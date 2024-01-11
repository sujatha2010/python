n = int(input("enter the number of numbers you want to calculate the average"))
sum = 0
for _ in range(n):
    # sum += int(input("enter the number"))
    sum = sum + int(input("enter the number"))
print("The avg is :", sum/n)
