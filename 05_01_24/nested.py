def my_function(x):
    def inner_function(y):
        return y * 2

    result_inner = inner_function(x)
    return result_inner + 5

input_value = 3
output_result = my_function(input_value)

print(f"The result of the nested functions for input {input_value} is: {output_result}")
