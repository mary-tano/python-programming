# Ловкач
import pygame as pg
import random
from dplayer import *
from dthing import *
from game import *

# Установка начальных значений
Red = (255,0,0)
Blue = (0,0,255)
Yellow = (255,255,0)
xMax, yMax = 800, 400

# Запуск Pygame, создание игровых элементов
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("Моя игра")
Window = pg.display.set_mode((xMax, yMax))
Figure = Player(20,30)
Ball = Thing("Bilder/ball1.png")
Ball.setPosition(xMax-50, yMax/2, True)
Arcade = Game(Yellow)

# Цикл событий
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False

    # Установка клавиш
    if event.type == pg.KEYDOWN :
      if event.key == pg.K_UP :
        Figure.setState(2)
        Arcade.getTime(True)
      if event.key == pg.K_DOWN :
        Figure.setState(1)
        Arcade.getTime(True)
        
  # Тестирование
  Time = Arcade.getTime(False)
  if Time > 200 :
    Figure.setState(0)
     
  # Перемещение мяча, сброс при необходимости
  if not Figure.isHit :
    Ball.move(-1, 0)
    if Ball.controlRestart(xMax-50, yMax/2) :
      Arcade.setScore(1, Blue)
  # Проверка, находится ли мяч в игровой зоне
  if (Ball.x < Figure.x+150) : 
    # Если игрок проиграл, игра заканчивается
    if not Figure.dodge(Ball.y, yMax/2) :
      Figure.isHit = True
      Arcade.showMessage("Игра окончена", Red)

  # Позиционирование спрайта в окне
  Window.fill(Yellow)
  Window.blit(Arcade.Text, (xMax/2, 10))
  Window.blit(Figure.Bild, (Figure.x, Figure.y))
  Window.blit(Ball.Bild, (Ball.x, Ball.y))
  pg.display.update()

# Завершение Pygame
pg.quit()

