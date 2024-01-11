x = "hello world"
y = {1: 'a', 2:'b'}

print('H' in x) #false
print('h' in x) # true

print('hello' not in x)
print(1 in y)
print('a' in y)

a = 10
b = 10

print(a is not b)
print(id(a))
print(id(b))