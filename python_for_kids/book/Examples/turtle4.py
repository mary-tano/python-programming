# Черепашья графика
from turtle import *

# Настройка окна
Width, Height = 600, 400
Window = Screen()
Window.title("Черепашка")
Window.setup(width=Width, height=Height)

# Прямоугольник и круг
penup()
goto(-245,150)
pendown()
for step in range(0,2) :
  forward(480)
  right(90)
  forward(290)
  right(90)
# Circle
penup()
goto(-25,-140)
pendown()
circle(145)

