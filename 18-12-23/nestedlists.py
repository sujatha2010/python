nested_list = [1, 2, [3, 4, 5], 6, [7, 8]]
element = nested_list[2][1]
print(element) 

for sublist in nested_list:
    if isinstance(sublist, list):
        for element in sublist:
            print(element)
    else:
        print(sublist)
nested_list = [1,2,[3,3], 6, [7,8]]
element = nested_list[2][1]
print(element)
for sublist in nested_list:
    if isinstance(sublist, list):
        for element in sublist:
            print(element)
        else:
            print(sublist)    