# Pygame графика
import pygame as pg
import random
from math import *
from bplayer import *

# Установка начальных значений
Green = (0,255,0)
xMax, yMax = 600, 400
degree = 0

# Запуск Pygame, создание игрового поля и персонажа
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("Моя игра")
Window = pg.display.set_mode((xMax, yMax))
Figure = Player(xMax/2-50, yMax/2-50)

# Случайное направление
xStep = random.randint(0,2)
if xStep == 0 :
  xStep = -1
yStep = random.randint(0,2)
if yStep == 0 :
  yStep = -1

# Цикл событий
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
    # Запрос мыши
    if event.type == pg.MOUSEBUTTONDOWN :
      (xPos, yPos) = pg.mouse.get_pos()
      if (xPos > Figure.x) and (xPos < Figure.x + 100) \
      and (yPos > Figure.y) and (yPos < Figure.y + 100) :
        Figure.destroy()   

  # Ограничение управления
  if (Figure.x < 0) or (Figure.x > xMax-110) :
    xStep = -xStep
  if (Figure.y < 0) or (Figure.y > yMax-110) :
    yStep = -yStep
    
  # Определение направления движения
  degree = atan2(-yStep, xStep)
  degree = degrees(degree) - 90
  Figure.rotate(degree)
 
  # Задержка движения
  if not Figure.isKilled :
    Figure.step(xStep, yStep)
    pg.time.delay(5)

  # Положение спрайта в окне (новое)
  Window.fill(Green)
  Window.blit(Figure.Bild, (Figure.x, Figure.y))
  pg.display.update()

# Завершение Pygame
pg.quit()

