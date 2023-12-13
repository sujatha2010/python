x = 5
y = 3
print(x != y)
x = 10
y = 5
print(x < y)
x = 5
y = 4
print(x >= y)
x = 5
print(x > 3 and x < 10)  #both statements are true in and condition

x = 3
print(x > 5 or x > 6)
x = 7
print(x <= 7 or x < 6)  # true if one of the statement is true

x = 5
print(not(x > 3 and x < 10)) # reverse the result, returns false if the result is true