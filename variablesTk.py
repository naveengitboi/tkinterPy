import tkinter as tk
from tkinter import ttk

app = tk.Tk()

app.title("New Work")
app.geometry("300x200")

input_value = tk.StringVar()
inputElement = ttk.Entry(master=app, textvariable=input_value)
inputElement.pack()

output_value = tk.StringVar()
outputEle = ttk.Label(master=app, text="Some random", textvariable=input_value)
outputEle.pack()

def submitFunc():
    inputElement["state"] = "disabled"

enterBtn = ttk.Button(master=app, text="Enter Btn", command=submitFunc)
enterBtn.pack()

def resetFunc():
    inputElement["state"] = "enabled"

resetEle = ttk.Button(master=app, text="Reset Btn", command=resetFunc)
resetEle.pack()


app.mainloop()