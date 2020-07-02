from tkinter import *

window = Tk()

def convert_all():
    grams.delete('1.0',END)
    pounds.delete('1.0',END)
    ounces.delete('1.0',END)
    value = float(user_value.get())
    g = value * 1000
    p = value * 2.205
    o = value * 35.274
    grams.insert(END,g)
    pounds.insert(END,p)
    ounces.insert(END,o)


kg = Label(window,text='kg')
kg.grid(row=0,column=0)

user_value = StringVar()
user_input = Entry(window,textvariable=user_value)
user_input.grid(row=0,column=1)

bt = Button(window,text='Convert', command=convert_all)
bt.grid(row=0,column=3)

grams = Text(window,height=1,width=20,borderwidth=2,relief="groove")
grams.grid(row=1,column=0)

pounds =Text(window,height=1,width=20,borderwidth=2,relief="groove")
pounds.grid(row=1,column=1)

ounces = Text(window,height=1,width=20,borderwidth=2,relief="groove")
ounces.grid(row=1,column=3)

window.mainloop()