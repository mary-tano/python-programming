# Pygame графика
import pygame as pg
from math import *

# Класс Player
class Player(pg.sprite.Sprite) :
  def __init__(self, xPos=0, yPos=0) :
    super().__init__()
    self.image = pg.image.load("Bilder\Insekt1.png")
    self.x, self.y = xPos, yPos
    self.Bild = self.image
  def rotate(self, degree) :
    self.Bild = pg.transform.rotate(self.image, degree)
  def move(self, distance, xx, yy) :
    self.x += xx
    self.y += yy
    distance -= 1
    return distance

# Установка начальных значений
Green = (0,255,0)
xMax, yMax = 600, 400
distance = 0
degree = 0

# Запуск Pygame, создание игрового поля и персонажа
pg.init()
pg.key.set_repeat(20,20)
Window = pg.display.set_mode((xMax, yMax))
Figure = Player(xMax/2-50, yMax/2-50)

# Цикл событий
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
    # Запрос мыши
    if event.type == pg.MOUSEBUTTONDOWN :
      (xPos, yPos) = pg.mouse.get_pos()
      ##--
      xDiff = xPos - Figure.x - 50
      yDiff = yPos - Figure.y - 50
      distance = sqrt(xDiff*xDiff + yDiff*yDiff)
      degree = atan2(-yDiff, xDiff)
      degree = degrees(degree) - 90
      xDiff /= distance
      yDiff /= distance
      Figure.rotate(degree)
  
  # Задержка движения 
  if distance > 5 :
    distance = Figure.move(distance, xDiff, yDiff)
    pg.time.delay(5)
    
  # Положение спрайта в окне (новое)
  Window.fill(Green)
  Window.blit(Figure.Bild, (Figure.x, Figure.y))
  pg.display.update()

# Завершение Pygame
pg.quit()

