# Графика
from tkinter import *
import random

# Константы света
Color = ["gray", "black", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Функция события
def buttonClick() :
  for Nr in range(0,32) :
    Color = Color[random.randint(0,7)]
    Font = random.randint(10,30)
    Graphic.create_text(random.randint(0,Width), random.randint(0,Width), \
    text="Привет!", fill=Color, font=("Arial", Font))
    
# Основная программа
Window = Tk()
Window.title("Графика")
Width = 500
Height = 330
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
Button = Button(Window, text="Давай напишем!", command=buttonClick)
Button.place(x=Width/2-60, y=Height/2-15, width=120, height=30)
Window.mainloop()

