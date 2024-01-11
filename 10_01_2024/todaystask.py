def getNotes(amountBalance, atm_notes, note):
    if(amountBalance > 0):
        notes = amountneeded//note
        if(notes > atm_notes):
            notes = atm_notes
        return notes
    return 0

atm2000 = int(input("Enter number of 2000$ notes available in ATM "))
atm500 = int(input("Enter number of 500$ notes available in ATM "))
atm100 = int(input("Enter number of 100$ notes available in ATM "))
atm20 = int(input("Enter number of 20$ notes available in ATM "))

amountneeded = int(input("Enter amount to be withdrawn "))
while(amountneeded%20 > 0):
    print("Invalid amount is entered for withdrawn, Amount should be multiple of 20$")
    amountneeded = int(input("Enter amount to be withdrawn "))


n2000 = getNotes(amountneeded, atm2000, 2000)
amountneeded = amountneeded - (n2000*2000)

n500 = getNotes(amountneeded, atm500, 500)
amountneeded = amountneeded - (n500*500)

n100 = getNotes(amountneeded, atm100, 100)
amountneeded = amountneeded - (n100*100)

n20 = getNotes(amountneeded, atm20, 20)
amountneeded = amountneeded - (n20*20)

if(amountneeded == 0):
    print(n2000, " 2000$ notes")
    print(n500, " 500$ notes")
    print(n100, " 100$ notes")
    print(n20, " 20$ notes")
else:
    print("we can not not dispense give amount")