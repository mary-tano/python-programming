# Черепашья графика
from turtle import *

# Настройка окна
Width, Height = 600, 400
Window = Screen()
Window.title("Черепашка")
Window.setup(width=Width, height=Height)

# Рисование
Path = 5 
degree = 45
while degree > 28 :
  Path += 2
  degree -= 0.2
  left(degree)
  forward(Path)
