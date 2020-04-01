# Рисование с помощью мыши
from tkinter import *

# Размеры окна
Width = 500
Height = 330

# Функция события
def mouseDraw(event):
   x = event.x - 1
   y = event.y - 1
   Graphic.create_oval( x, y, x+3, y+3)

# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.bind("<B1-Motion>", mouseDraw)
Graphic.pack()
Display = Label(Window, text = "Рисование с помощью мыши")
Display.pack(side="bottom")
Window.mainloop()

