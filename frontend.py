from tkinter import *
from backend import Database


database = Database("book.db")

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        print(selected_tuple)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for rows in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get() ):
        list1.insert(END,rows)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def update_command():
    database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    

def delete_command():
    database.delete(selected_tuple[0])


top=Tk()
top.wm_title("ABHI BOOKSTORE")

l1=Label(top,text="TITLE")
l1.grid(row=0,column=0)

title_text=StringVar()
e1=Entry(top,textvariable=title_text)
e1.grid(row=0,column=1)

l2=Label(top,text="AUTHOR")
l2.grid(row=0,column=2)

author_text=StringVar()
e2=Entry(top,textvariable=author_text)
e2.grid(row=0,column=3)

l3=Label(top,text="YEAR")
l3.grid(row=1,column=0)

year_text=StringVar()
e3=Entry(top,textvariable=year_text)
e3.grid(row=1,column=1)

l4=Label(top,text="ISBN")
l4.grid(row=1,column=2)

isbn_text=StringVar()
e4=Entry(top,textvariable=isbn_text)
e4.grid(row=1,column=3)



b1=Button(top,text="View all",width=12,command = view_command)
b1.grid(row=2,column=0)

b2=Button(top,text="Search Entry",width=12,command = search_command)
b2.grid(row=3,column=0)

b3=Button(top,text="Add Entry",width=12, command = add_command)
b3.grid(row=4,column=0)

b4=Button(top,text="Update",width=12, command = update_command)
b4.grid(row=5,column=0)

b5=Button(top,text="Delete",width=12, command = delete_command)
b5.grid(row=9,column=1)

b6=Button(top,text="Close",width=12, command = top.destroy)
b6.grid(row=9,column=3)


list1=Listbox(top,height=6, width = 40)
list1.grid(row=3,column=1,rowspan=6,columnspan=3)


sb1=Scrollbar(top)
sb1.grid(row=3,column=4,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


top.mainloop()
