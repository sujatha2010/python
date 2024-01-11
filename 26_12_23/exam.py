year = int(input("enter year"))
print("enter the month, possible values are jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec")
month = input()

if (month == "jan" or month == "mar" or month == "may" or month == "jul" or month == "aug" or month == "oct" or month == "dec"):
    print("num of days given month and year is 31")
elif(month == "apr" or month== "jun" or month == "sep" or month == "nov"):
    print("num of days given month and year is 30")
elif(year % 4 == 0 and month == "feb"):
    print("num of days given month and year is 29")
elif(month == "feb"):
    print("num of days given month and year is 28")
else:
    print("given invalid month")
       
