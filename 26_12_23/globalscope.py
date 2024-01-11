# x = 300
# def myfunc():
#     print(x)
# myfunc()
# print(x)

def musuji():
   global x
   x = 200
def innerfunc():
    print(x)
    innerfunc()
musuji()
print(x)

