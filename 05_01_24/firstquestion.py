def add_without_operators(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def subtract_without_operators(a, b):
    return add_without_operators(a, add_without_operators(~b, 1))

num1 = int(input("Enter First number\n"))
num2 = int(input("Enter Second number\n"))

sum_result = add_without_operators(num1, num2)
difference_result = subtract_without_operators(num1, num2)

print("Sum: " + str(sum_result))
print("Difference: " + str(difference_result))