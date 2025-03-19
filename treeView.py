import tkinter as tk 
from tkinter import ttk
from random import choice


app = tk.Tk()

app.title("Tree view")

firstNames = ["Naveen", "Chandrakala", "Anajaneyulu", "Nandini", "Purnima"]
lastNames = ["Jangiti", "Jangiti", "Jangiti", "Jangiti", "Bolluru"]
emails = []
for i in range(len(firstNames)):
    mail = f'{firstNames[i]}.{lastNames[i]}@gmail.com'
    emails.append(mail)

table = ttk.Treeview(master=app, columns=('first', 'last' , 'email'), show="headings")
table.heading('first', text="First Name")
table.heading('last', text="SurName")
table.heading('email', text="Email")
table.pack(fill="both", expand=True)


for i in range(len(firstNames)):
    data = (firstNames[i], lastNames[i], emails[i])
    table.insert(parent='', index=0, values=data)

def tableInfoView(_):
    for i in table.selection():
        print(table.item(i)['values'])

def deleteItem(_):
    for i in table.selection():
        table.delete(i)


table.bind("<<TreeviewSelection>>", tableInfoView)
table.bind("<Delete>", deleteItem)

app.mainloop()