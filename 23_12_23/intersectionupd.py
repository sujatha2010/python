x = {"apple", "banana", "orange"} 
y = {"rose", "jasmine", "apple"}
# x.intersection_update(y)
# print(x) same values are allowed in this condition different values are not alloowed.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

x.symmetric_difference_update(y)
# print(x) same values are not allowed only allowed in different values