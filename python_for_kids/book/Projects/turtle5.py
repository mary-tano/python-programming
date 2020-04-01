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
degree = 0
for Nr in range(1,13) :
  degree += 30
  home()
  left(degree)
  forward(500)
  forward(-500)
