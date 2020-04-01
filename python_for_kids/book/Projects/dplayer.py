# Pygame графика
import pygame as pg

# Класс Player
class Player(pg.sprite.Sprite) :
  image = []
  Dname = ""
  def __init__(self, xPos=0, yPos=0) :
    super().__init__()
    self.image.append(pg.image.load("Bilder\DoStand.png"))
    self.image.append(pg.image.load("Bilder\DoDuck.png"))
    self.image.append(pg.image.load("Bilder\DoJump.png"))
    self.x, self.y = xPos, yPos
    self.Bild = self.image[0]
    self.Width = self.Bild.get_width()
    self.Height = self.Bild.get_height()
    self.rect = self.Bild.get_rect()
    self.isHit = False
    self.Status = 0
  def setState(self, Nr) :
    self.Status = Nr
    self.Bild = self.image[Nr]
  def dodge(self, yPos, yMiddle) :
    if (yPos < yMiddle and self.Status == 1) \
    or (yPos > yMiddle and self.Status == 2) :
      return True
    else :
      return False   
  def destroy(self) :
    self.image.append(pg.image.load("Bilder\DoDie.png"))
    self.Bild = self.image[3]
    self.isHit = True
    
  # От старого класса
  def rotate(self, degree) :
    self.Bild = pg.transform.rotate(self.image[0], degree)
  def move(self, xx, yy) :
    self.x += xx
    self.y += yy


