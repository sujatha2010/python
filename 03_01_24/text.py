from tkinter import*
base=Tk()
base.title("REGISTRATION FROM")
base.geometry('500x500')

lab1=Label(base,text="REGISTATION FROM",width=20,font="bold")
lab1.place(x=90,y=53)

lab2=Label(base,text="Full Name",width=20,font=("bold",10))
lab2.place(x=80,y=130)
entry2=Entry(base)
entry2.place(x=240,y=130)



mainloop()