import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Buttons")
app.geometry("300x200")


#basic btn
def basicBtn():
    pass
button = ttk.Button(master=app, text="Simple Btn", command=basicBtn)
button.pack()


def checkBtn():
    print(isChecked.get())

#check btn
isChecked = tk.BooleanVar()
checkBtn = ttk.Checkbutton(master=app, text="Check Box", command=checkBtn, variable=isChecked)
checkBtn.pack()


#radion btns
radioValue = tk.StringVar()
radioBtn1 = ttk.Radiobutton(master=app, text="Radion Btn 1", value="Rad 1", variable=radioValue, command=lambda: print(radioValue.get()))
radioBtn1.pack()

radioBtn2 = ttk.Radiobutton(master=app, text="Radion Btn 2", value="Rad 2", variable=radioValue, command=lambda: print(radioValue.get()))
radioBtn2.pack()

app.mainloop()