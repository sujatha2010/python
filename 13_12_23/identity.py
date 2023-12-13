x = ["suji", "kiran"]
y = ["suji", "kiran"]
z = x
print(x is z)# returns True because z is the same object as x

print(x is y)# return false beacuse x is not same object as y, even if they have same content
print(x == y) 
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["sujatha", "kiran"]
y = ["kiran", "sujatha"]
z = x

print(x is not y) #return true if both variables are not the same object
print(x is not z)
print(x is not y)