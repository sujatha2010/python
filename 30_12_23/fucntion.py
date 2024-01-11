# def kiran(a):
#     print(a)
# kiran(1)

# def kiran(a,b):
#     print(a,b)   # multiple params and arguments
# kiran(1, "suji")

# def suji(*a):
#     print(a)  # orbitary aruguments in this case we can store multiple values(arguments) to one param.
# suji(1, 2 ,3)


def myfunction(**b):
    print(b)                #key vlues pairs  output format is dictionary format
myfunction(name = "suji", age = 25)

def function_name(name,age):
    print("this is fucntion", name, age)
function_name('kiran', 23)

