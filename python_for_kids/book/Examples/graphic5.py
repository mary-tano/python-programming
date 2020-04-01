# Графика в Python
from tkinter import *
import random

# Константы цвета
Color = ["gray", "black", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Функция события
def buttonClick() :
  for Nr in range(0,32) :
    Dye = Color[random.randint(0,7)]
    Font = random.randint(10,30)
    Graphic.create_text(random.randint(0,Breadth), random.randint(0,Breadth), \
    text="Привет!", fill=Dye, font=("Arial", Font))
    
# Основная программа
Window = Tk()
Window.title("Графика")
Breadth = 500
Highness = 330
Window.config(width=Breadth, height=Highness)
Graphic = Canvas(Window, width=Breadth, height=Highness)
Graphic.pack()
Button = Button(Window, text="Посмотреть!", command=buttonClick)
Button.place(x=Breadth/2-60, y=Highness/2-15, width=120, height=30)
Window.mainloop()

