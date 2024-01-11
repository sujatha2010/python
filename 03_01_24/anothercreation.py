from tkinter import*

parent = Tk()
# parent.iconbitmap('/suji.png')
parent.title("hi kiran")

def say_hello():
    name = userinput.get() #get cheskuntundhi userinput ni
    greeting = 'hello ' + name +  ' ! '

    if name != '':
     my_text.config(text=greeting) # override cheyyali or re write cheyyali
     userinput.delete(0, END)
    else:
       my_text.config(text = 'enter your name')


userinput = Entry(parent, font=('aerial', 30))
userinput.pack(padx=30, pady=30)
my_text = Label(parent, text="enter your name", font=('aerial', 20))
my_text.pack(pady=5)


button = Button(parent, text= "say hello", font=('aerial', 30), command=say_hello)
button.pack(padx=20, pady=30)

parent.mainloop()

