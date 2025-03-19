import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Sliders")

scaleValue = tk.DoubleVar(value=10)
scale = ttk.Scale(master=app, command=lambda event: print(scaleValue.get()), from_=0 ,to =25, length=300, orient="horizontal", variable=scaleValue)
scale.pack()


progressBar = ttk.Progressbar(master=app, variable=scaleValue, maximum=25, orient="horizontal", length=300)
progressBar.pack()


app.mainloop()