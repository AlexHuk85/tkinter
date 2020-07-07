import backend
from tkinter import *

window = Tk()

#--------------------------------------------------functions
def view_command():
    listbox.delete(0,END)
    for row in backend.view():
        listbox.insert(END,row)

def search_command():
    pass


# ------------------------------------------------------Label
label1 = Label(window,text='Title')
label1.grid(row=0,column=0)

label2 = Label(window,text='Author')
label2.grid(row=0,column=2)

label3 = Label(window,text='Year')
label3.grid(row=1,column=0)

label4 = Label(window,text='ISBN')
label4.grid(row=1,column=2)

# --------------------------------------------------------Entry
entry_title_value = StringVar()
entry_title = Entry(window,textvariable=entry_title_value)
entry_title.grid(row=0,column=1)

entry_author_value = StringVar()
entry_author = Entry(window,textvariable=entry_author_value)
entry_author.grid(row=0,column=3)

entry_year_value = StringVar()
entry_year = Entry(window,textvariable=entry_year_value)
entry_year.grid(row=1,column=1)

entry_isbn_value = StringVar()
entry_isbn = Entry(window,textvariable=entry_isbn_value)
entry_isbn.grid(row=1,column=3)

# --------------------------------------------Listbox + scrollbar
listbox = Listbox(window,height=8,width=30)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox.yview)

# ---------------------------------------------------Buttons
view_button = Button(window,text='View all',width=20,command=view_command)
view_button.grid(row=2,column=3)

search_button = Button(window,text='Search data',width=20,command=search_command)
search_button.grid(row=3,column=3)

add_button = Button(window,text='Add data',width=20)
add_button.grid(row=4,column=3)

update_button = Button(window,text='Update',width=20)
update_button.grid(row=5,column=3)

delete_button = Button(window,text='Delete',width=20)
delete_button.grid(row=6,column=3)

close_button = Button(window,text='Close',width=20)
close_button.grid(row=7,column=3)




#-----------------------------------------Window mainloop
window.mainloop()