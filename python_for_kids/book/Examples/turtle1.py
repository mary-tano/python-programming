# Черепашья графика
from turtle import *

# Настройка окна
Width, Height = 600, 400
Window = Screen()
Window.title("Черепашка")
Window.setup(width=Width, height=Height)

# Рисование
shape("turtle")
for step in range(0,4) :
  forward(150)
  left(90)


