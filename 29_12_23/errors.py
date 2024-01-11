
# try:
#     # print(x) error occurse x is not defined
#     # print("x")
#     print('a'+33)
# except:
#     print("error")
# else:
#     print("no error")
# finally:
#     print("always")

try:
    print('a'+ 33)
except TypeError:
    print("type error")
except ValueError:
    print("value error")
else:
    print("no error occur")
finally:
    print("always")
 