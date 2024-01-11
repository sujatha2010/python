def outer_function():
    a = 20
    print('a = ', a)
    def inner_function():

        a  = 25

        print('a =', a)
    inner_function()
    print('a =', a)


# a =15

# print('a = ', a)
outer_function()


    