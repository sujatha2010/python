def add_numbers(a, b):
    sum_result = a + b
    return sum_result
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")
