# Pygame графика
import pygame as pg

# Класс Player
class Player(pg.sprite.Sprite) :
  def __init__(self, xPos=0, yPos=0) :
    super().__init__()
    self.image = pg.image.load("Bilder\Insekt1.png")
    self.x, self.y = xPos, yPos
    self.Bild = self.image
  def rotate(self, degree) :
    self.Bild = pg.transform.rotate(self.image, degree)

# Установка начальных значений
Green = (0,255,0)
Richtung = 0

# Запуск Pygame, создание игрового поля и персонажа
pg.init()
pg.key.set_repeat(20,20)
Window = pg.display.set_mode((600, 400))
Figure = Player(250, 150)

# Цикл событий
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
    # Установка клавиш
    if event.type == pg.KEYDOWN :
      if event.key == pg.K_LEFT :
        Richtung = 1
        Figure.x -= 5
      if event.key == pg.K_RIGHT :
        Richtung = 3
        Figure.x += 5
      if event.key == pg.K_UP :
        Richtung = 0
        Figure.y -= 5
      if event.key == pg.K_DOWN :
        Richtung = 2
        Figure.y += 5
      Figure.rotate(Richtung*90) 
    # Положение спрайта в окне (новое)
    Window.fill(Green)
    Window.blit(Figure.Bild, (Figure.x, Figure.y))
    pg.display.update()

# Завершение Pygame
pg.quit()
