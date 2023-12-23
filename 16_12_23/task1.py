def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

input_number = int(input("Enter a number: "))
result = "prime" if is_prime(input_number) else "not prime"
print(f"{input_number} is {result}.")
