# Черепашья графика
from turtle import *
import random

# Настройка окна
Width, Height = 600, 400
Window = Screen()
Window.title("Черепашка")
Window.setup(width=Width, height=Height)

# Рисование
for step in range(0,10) :
  forward(random.randint(10,100))
  left(random.randint(60,90))

