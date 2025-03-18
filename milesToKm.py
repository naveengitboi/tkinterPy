import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Demo")
window.geometry("300x200")

initialOutput = "Converted Texts"

# functionalities
def convertFunction():
    milesInput = input_value.get()
    kmOutput = f'{milesInput*1.61} Km'
    output_value.set(kmOutput)


#title
header = ttk.Label(master = window, text="Miles to KM Conversion", font="Poppins 24 bold")

header.pack()

#input Div

inputContainer = ttk.Frame(master = window)

input_value = tk.IntVar()
inputEntry = ttk.Entry(master=inputContainer, textvariable=input_value)
inputButton = ttk.Button(master = inputContainer, text="Generate", command=convertFunction)

inputEntry.pack(side="left", padx=10)
inputButton.pack()
inputContainer.pack(pady=10)


#outpute text
output_value = tk.StringVar()
outputText = ttk.Label(master=window, text=initialOutput, font="Poppins 24 bold", textvariable=output_value)

outputText.pack()


#runing
window.mainloop()