# Ловкач
import pygame as pg
import random
from dplayer import *

# Установка начальных значений
Yellow = (255,255,0)
xMax, yMax = 800, 400

# Запуск Pygame, создание игрового поля и персонажа
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("Моя игра")
Window = pg.display.set_mode((xMax, yMax))
Figure = Player(20,30)

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
      if event.key == pg.K_DOWN :
        Figure.setState(1)
      if event.key == pg.K_RETURN :
        Figure.setState(0)
        
  # Позиционирование спрайта в окне
  Window.fill(Yellow)
  Window.blit(Figure.Bild, (Figure.x, Figure.y))
  pg.display.update()

# Завершение Pygame
pg.quit()

