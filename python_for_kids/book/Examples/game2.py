# Pygame графика
import pygame as pg

# Класс Player
class Player(pg.sprite.Sprite) :
  def __init__(self) :
    super().__init__()
    self.image = pg.image.load("Bilder\Insekt1.png")

# Определение цветов
Green = (0,255,0)

# Запуск Pygame, создание игры
pg.init()
Window = pg.display.set_mode((600, 400))
Window.fill(Green)

# Создание персонажа
Figure = Player()

# Цикл событий
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
  # Позиционирование спрайта в окне
  Window.blit(Figure.image, (250, 150))
  pg.display.update()

# Завершение Pygame
pg.quit()
