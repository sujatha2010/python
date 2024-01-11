def swap_case(s):
    swap_string = ""
    for char in s:
        if char.isupper():
            swap_string += char.lower()
        else:
            swap_string += char.upper()
    return swap_string
userinput = input("Enter a string:")
result = swap_case(userinput)
print(result)

    
