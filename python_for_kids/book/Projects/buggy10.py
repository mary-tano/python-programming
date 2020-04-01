# Pygame графика
import pygame as pg
import random
from math import *
from bplayer import *
from game import *

# Установка начальных значений
Green = (0,255,0)
Blue = (0,0,255)
xMax, yMax = 800, 600
degree = 0
bugMax = 5

# Запуск Pygame, создание игровых элементов
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("My Game")
Window = pg.display.set_mode((xMax, yMax))
Game = Game(Green)

# Создание игровых персонажей
Figure = []
for Nr in range(0,bugMax) :
  xPos = random.randint(100,xMax-100)
  yPos = random.randint(50,yMax-100)
  Figure.append(Player(xPos, yPos))

# Случайное направление для каждой фигуры
xStep = []
yStep = []
for Nr in range(0,bugMax) :
  xStep.append(random.randint(0,2))
  if xStep[Nr] == 0 :
    xStep[Nr] = -1
  yStep.append(random.randint(0,2))
  if yStep[Nr] == 0 :
    yStep[Nr] = -1

# Цикл событий
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
    # Запрос мыши
    if event.type == pg.MOUSEBUTTONDOWN :
      (xPos, yPos) = pg.mouse.get_pos()
      for Nr in range(0,bugMax) :
        if (xPos > Figure[Nr].x) and (xPos < Figure[Nr].x + 100) \
        and (yPos > Figure[Nr].y) and (yPos < Figure[Nr].y + 100) :
          if not Figure[Nr].isKilled :
            Game.setScore(50, Blue)
          Figure[Nr].destroy()

  # Ограничение управления
  for Nr in range(0,bugMax) :
    if (Figure[Nr].x < 0) or (Figure[Nr].x > xMax-110) :
      xStep[Nr] = -xStep[Nr]
    if (Figure[Nr].y < 0) or (Figure[Nr].y > yMax-110) :
      yStep[Nr] = -yStep[Nr]
    
  # Определение направления движения
  for Nr in range(0,bugMax) :
    degree = atan2(-yStep[Nr], xStep[Nr])
    degree = degrees(degree) - 90
    Figure[Nr].rotate(degree)
 
  # Задержка движения
  for Nr in range(0,bugMax) :
    if not Figure[Nr].isKilled :
      Figure[Nr].step(xStep[Nr]*2, yStep[Nr]*2)
  pg.time.delay(5)

  # Положение спрайта в окне (новое)
  Window.fill(Green)
  Window.blit(Game.Text, (xMax/3, 10))
  for Nr in range(0,bugMax) :
    Window.blit(Figure[Nr].Bild, (Figure[Nr].x, Figure[Nr].y))
  pg.display.update()

# Завершение Pygame
pg.quit()

