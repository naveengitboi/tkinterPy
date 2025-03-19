import tkinter as tk


app = tk.Tk()
app.title("Drawing Board")
app.geometry("300x300")


canvas = tk.Canvas(master=app, background="white")
canvas.pack()

def drawOnCanvas(event):
    x, y = event.x, event.y
    left = x - brushSize/2 
    top = y - brushSize/2 
    right = x + brushSize/2 
    bottom = y + brushSize/2 
    canvas.create_oval((left,top, right, bottom), fill="black")

def changeBrushSize(event):
    global brushSize
    if event.delta > 0:
        brushSize += 2
    else:
        brushSize -= 2
    
    brushSize = max(0, min(20, brushSize))

brushSize = 2
canvas.bind("<Motion>", drawOnCanvas)
canvas.bind("<MouseWheel>", changeBrushSize)


app.mainloop()



