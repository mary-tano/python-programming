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
  for Nr in range(0,84) :
    Dye = Color[random.randint(0,7)]
    Graphic.create_line(0, Nr*4, Breadth, Highness-Nr*4, fill=Dye)
    Graphic.create_line(Nr*6, 0, Breadth-Nr*6, Highness, fill=Dye)   

# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Breadth, height=Highness)
Graphic = Canvas(Window, width=Breadth, height=Highness)
Graphic.pack()
Button = Button(Window, text="Посмотреть!", command=buttonClick)
Button.place(x=Breadth/2-60, y=Highness/2-15, width=120, height=30)
Window.mainloop()

