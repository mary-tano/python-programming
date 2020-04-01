# Pygame графика
import pygame as pg

# Класс Player
class Player(pg.sprite.Sprite) :
  def __init__(self, xPos=0, yPos=0) :
    super().__init__()
    self.image = pg.image.load("Bilder\Insekt2.png")
    self.x, self.y = xPos, yPos
    self.Bild = self.image
    self.isKilled = False
  def rotate(self, degree) :
    self.Bild = pg.transform.rotate(self.image, degree)
  def move(self, distance, xx, yy) :
    self.x += xx
    self.y += yy
    distance -= 1
    return distance
  def step(self, xx, yy) :
    self.x += xx
    self.y += yy
  def destroy(self) :
    self.image = pg.image.load("Bilder\Insekt2X.png")
    self.Bild = self.image
    self.isKilled = True

