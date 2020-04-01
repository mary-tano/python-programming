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
  for Nr in range(0,48) :
    Dye = Color[random.randint(0,7)]
    Graphic.create_rectangle(Nr*4, Nr*3, Breadth-Nr*4, Highness-Nr*3, fill=Dye)
    
# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Breadth, height=Highness)
Graphic = Canvas(Window, width=Breadth, height=Highness)
Graphic.pack()
Button = Button(Window, text="Посмотреть!", command=buttonClick)
Button.place(x=Breadth/2-60, y=Highness/2-15, width=120, height=30)
Window.mainloop()

