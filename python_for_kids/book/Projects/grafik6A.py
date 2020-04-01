# Графика
from tkinter import *
import random

# Константы света
Color = ["white", "gray", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Функция события
def buttonClick() :
  for Nr in range(0,5000) :
    x = random.randint(0,Width)
    y = random.randint(0,Height)
    Color = Color[random.randint(0,7)]
    Graphic.create_oval(x,y, x+1, y+1, fill=Color)
    
# Основная программа
Window = Tk()
Window.title("Графика")
Width = 500
Height = 330
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height, background="black")
Graphic.pack()
Button = Button(Window, text="Сверкание!", command=buttonClick)
Button.place(x=Width/2-60, y=Height-40, width=120, height=30)
Window.mainloop()

