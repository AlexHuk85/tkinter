from tkinter import *

window = Tk()

kg = Label(window,text='kg')
kg.grid(row=0,column=0)

user_input = Entry(window)
user_input.grid(row=0,column=1)

bt = Button(window,text='Convert')
bt.grid(row=0,column=3)

grams = Text(window,height=1,width=20,borderwidth=2,relief="groove")
grams.grid(row=1,column=0)

pounds =Text(window,height=1,width=20,borderwidth=2,relief="groove")
pounds.grid(row=1,column=1)

ounces = Text(window,height=1,width=20,borderwidth=2,relief="groove")
ounces.grid(row=1,column=3)

window.mainloop()