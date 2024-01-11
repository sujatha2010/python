from tkinter import*

top = Tk()

top.geometry("200x200")


checkvar1 = IntVar()  
  
checkvar2 = IntVar()  


cbtn1 = Checkbutton(top, text = 'java', variable=checkvar1, onvalue=1,offvalue=0 , height=2, width=10)
cbtn2 = Checkbutton(top, text = 'java', variable=checkvar2, onvalue=1,offvalue=0 , height=2, width=10)


cbtn1.pack()
cbtn2.pack()

top.mainloop()