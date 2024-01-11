# def mySquare(x):
#     return x*x
# def calculate(fun):
#     print(fun(2))

# # d = mySquare
# # calculate(d)
# calculate(mySquare)

def mySquare(x):
    return x*x
def myCube(x):
    return x*x*x
def calculate(fun, arg):
    print(fun(arg))

# d = mySquare
# calculate(d)
calculate(mySquare, 2)
calculate(myCube,2)
