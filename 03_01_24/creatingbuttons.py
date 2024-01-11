from tkinter import*

MW = Tk()

def clicked():
    mylabel = Label(MW, text="chintu", font=("aerial", 20))
    mylabel.pack(pady=10)

user_input = Entry(width=20, font=('aerial', 20))   #entry method
user_input.pack(padx=30, pady=40)

my_button = Button(MW, text="sujikiran", font=('aeral', 20), command= clicked)
my_button.pack(padx=50, pady=30,)


MW.mainloop()