from tkinter import*

mw = Tk()
mylabel1 = Label(mw, text='hi everyone', font=('aerial', 20), fg='red')
mylabel2 = Label(mw, text='hi kiran how are you', font=('aerial', 20), fg='green')
mybutton = Button(mw, text='clik me', font=('aerial', 20), bg='#1a751d', activebackground='blue')
mylabel1.grid(row=0, column=0, padx=20, pady=20)
mylabel2.grid(row=1, column=0, padx=20, pady=30)
mybutton.grid(row=2, column=1,padx=30, pady=20)
mw.mainloop()