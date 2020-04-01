# Графика в Python
from tkinter import *
import random

# Константы цвета
Color = ["white", "gray", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Функция события
def buttonClick() :
  for Nr in range(0,5000) :
    x = random.randint(0,Breadth)
    y = random.randint(0,Highness)
    Dye = Color[random.randint(0,7)]
    Graphic.create_oval(x,y, x+1, y+1, fill=Dye)
    
# Основная программа
Window = Tk()
Window.title("Графика")
Breadth = 500
Highness = 330
Window.config(width=Breadth, height=Highness)
Graphic = Canvas(Window, width=Breadth, height=Highness, background="black")
Graphic.pack()
Button = Button(Window, text="Посмотреть!", command=buttonClick)
Button.place(x=Breadth/2-60, y=Highness-40, width=120, height=30)
Window.mainloop()

