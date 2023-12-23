thisdict = {
    "brand" : "ford",
    "model" : "suji",
    "model" : "suji1",
    "colors" : ["red", "green", "blue"]
}
print(thisdict)
print(len(thisdict))
print(thisdict)


listdict = dict(name = "jhon", age= 36, country="norway")
print(len(listdict))
thislistssdict = dict(name = "jhon", age = 28)
print(thislistssdict)

stud = {
    "name" : "suji",
    "country": "suji"
}
print(stud)

emp_dict = {}
stud_details = {"nickname": "suji", "age": 25}
stud_details.keys()

stu_det = {"flower":"red", "rose":"yello"}
x=stu_det.get("flower")
print(x)

stud_details = {"5GG":"Kufli", "5AG":"Dumbo", "5FF":"Kimble",}
y = stud_details.get("5AG")
print(y)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("yes, 'model' is one of the key ")

    thisdicts = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)
thisdict["color"] = "red"
print(x)