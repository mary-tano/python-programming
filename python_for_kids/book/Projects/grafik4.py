# Графика
from tkinter import *
import random

# Размеры окна
Width = 500
Height = 330

# Константы света
Color = ["gray", "black", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Функция события
def buttonClick() :
  Color = Color[random.randint(0,7)]
  Score = [(20,Height-20), (Width/2,20), (Width-20,Height-20)]
  Graphic.create_polygon(Score, fill=Color)
    
# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
Button = Button(Window, text="Давай посмотрим!", command=buttonClick)
Button.place(x=Width/2-60, y=Height/2+30, width=120, height=30)
Window.mainloop()

