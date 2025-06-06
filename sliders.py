import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
app = tk.Tk()
app.title("Sliders")

scaleValue = tk.DoubleVar(value=10)
scale = ttk.Scale(master=app, command=lambda event: print(scaleValue.get()), from_=0 ,to =25, length=300, orient="horizontal", variable=scaleValue)
scale.pack()


progressBar = ttk.Progressbar(master=app, variable=scaleValue, maximum=25, orient="horizontal", length=300)
progressBar.pack()


scrolleTextBox = scrolledtext.ScrolledText(master=app, width=50, height=5)
scrolleTextBox.pack()

app.mainloop()