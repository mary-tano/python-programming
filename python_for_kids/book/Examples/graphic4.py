# Графика в Python
from tkinter import *
import random

# Размеры окна
Breadth = 500
Highness = 330

# Константы цвета
Color = ["gray", "black", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Функция события
def buttonClick() :
  Dye = Color[random.randint(0,7)]
  Point = [(20,Highness-20), (Breadth/2,20), (Breadth-20,Highness-20)]
  Graphic.create_polygon(Point, fill=Dye)
    
# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Breadth, height=Highness)
Graphic = Canvas(Window, width=Breadth, height=Highness)
Graphic.pack()
Button = Button(Window, text="Посмотреть!", command=buttonClick)
Button.place(x=Breadth/2-60, y=Highness/2+30, width=120, height=30)
Window.mainloop()

