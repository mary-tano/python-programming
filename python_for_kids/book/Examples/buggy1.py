# Pygame графика
import pygame as pg

# Класс Player
class Player(pg.sprite.Sprite) :
  def __init__(self, xPos=0, yPos=0) :
    super().__init__()
    self.image = pg.image.load("Bilder\Insekt1.png")
    self.x, self.y = xPos, yPos

# Установка начальных значений
Green = (0,255,0)

# Запуск Pygame, создание игрового поля и персонажа
pg.init()
pg.key.set_repeat(20,20)
Window = pg.display.set_mode((600, 400))
Figure = Player(250, 150)
Window.fill(Green)

# Цикл событий
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
    # Установка клавиш
    if event.type == pg.KEYDOWN :
      if event.key == pg.K_LEFT :
        Figure.x -= 5
      if event.key == pg.K_RIGHT :
        Figure.x += 5
      if event.key == pg.K_UP :
        Figure.y -= 5
      if event.key == pg.K_DOWN :
        Figure.y += 5
      
  # Положение спрайта в окне (новое)
  
  Window.blit(Figure.image, (Figure.x, Figure.y))
  pg.display.update()

# Завершение Pygame
pg.quit()
