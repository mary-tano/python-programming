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
  for Nr in range(0,84) :
    Color = Color[random.randint(0,7)]
    Graphic.create_line(0, Nr*4, Width, Height-Nr*4, fill=Color)
    Graphic.create_line(Nr*6, 0, Width-Nr*6, Height, fill=Color)   

# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
Button = Button(Window, text="Давай посмотрим!", command=buttonClick)
Button.place(x=Width/2-60, y=Height/2-15, width=120, height=30)
Window.mainloop()

