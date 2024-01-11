def apply_operation(func, x, y):
    return func(x, y)
def add(x, y):
    return x + y 
print()

def multiply(x, y):
    return x * y
result_add = apply_operation(add, 3, 4)
result_multiply = apply_operation(multiply, 3, 4)
print("Result of add operation:", result_add) 
print("result of multiply operation:", result_multiply)
