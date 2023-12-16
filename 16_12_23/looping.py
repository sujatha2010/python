thislist = ["suji", "apple"]
for x in thislist:
    print(x)

thislist = ["apple", "suji"]
i = 0
while i < len(thislist):
    print(thislist)
    i = i + 1
list4 = ["apple", "suji", "orange"]
[print(x)for x in thislist]

fruits = ["apple", "banana", "suji"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)