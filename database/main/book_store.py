import backend
from tkinter import *



#--------------------------------------------------functions
def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        print(index)
        selected_tuple = listbox.get(index)
        entry_title.delete(0,END)
        entry_title.insert(END,selected_tuple[1])
        entry_author.delete(0,END)
        entry_author.insert(END,selected_tuple[2])
        entry_year.delete(0,END)
        entry_year.insert(END,selected_tuple[3])
        entry_isbn.delete(0,END)
        entry_isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    listbox.delete(0,END)
    for row in backend.view():
        listbox.insert(END,row)

# -------------------------------------!! TODO, search key word
def search_command():
    listbox.delete(0,END)
    for row in backend.search(entry_title_value.get(),entry_author_value.get(),entry_year_value.get(),entry_isbn_value.get()):
        listbox.insert(END,row)

def add_command():
    backend.insert(entry_title_value.get(),entry_author_value.get(),entry_year_value.get(),entry_isbn_value.get())
    listbox.delete(0,END)
    listbox.insert(END,(entry_title_value.get(),entry_author_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(entry_title_value.get(),entry_author_value.get(),entry_year_value.get(),entry_isbn_value.get(),selected_tuple[0])
    view_command()

# --------------------------------------------Window Start
window = Tk()

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

listbox.bind('<<ListboxSelect>>',get_selected_row)

# ---------------------------------------------------Buttons
view_button = Button(window,text='View all',width=20,command=view_command)
view_button.grid(row=2,column=3)

search_button = Button(window,text='Search data',width=20,command=search_command)
search_button.grid(row=3,column=3)

add_button = Button(window,text='Add data',width=20,command=add_command)
add_button.grid(row=4,column=3)

update_button = Button(window,text='Update',width=20,command=update_command)
update_button.grid(row=5,column=3)

delete_button = Button(window,text='Delete',width=20,command=delete_command)
delete_button.grid(row=6,column=3)

close_button = Button(window,text='Close',width=20,command=window.destroy)
close_button.grid(row=7,column=3)

#-----------------------------------------Window mainloop
window.mainloop()