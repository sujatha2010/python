trw = float(input("Enter Total weight of the residue \n"))
tmn = float(input("Enter Total amount of manure \n"))

nm = 0.3 * trw

emn = max(0, tmn - nm)

print("Extra amount of manure need is " + str(round(emn, 2)))

