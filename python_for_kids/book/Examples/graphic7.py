# Рисование с помощью мыши
from tkinter import *

# Размеры окна
Breadth = 500
Highness = 330

# Функция события
def mouseDraw(event):
   x = event.x - 1
   y = event.y - 1
   Graphic.create_oval( x, y, x+3, y+3)

# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Breadth, height=Highness)
Graphic = Canvas(Window, width=Breadth, height=Highness)
Graphic.bind("<B1-Motion>", mouseDraw)
Graphic.pack()
Anzeige = Label(Window, text = "Рисование мышью")
Anzeige.pack(side="bottom")
Window.mainloop()

