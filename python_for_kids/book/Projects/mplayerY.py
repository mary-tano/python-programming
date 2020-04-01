from tkinter import *

# Класс Player
class Player :
  Bild = [0]
  BildNr = 0
  Figure = 0
  LR = -1
  
  def __init__(self, graphic) :
    self.Graphic = graphic
    for Nr in range(1,9) :
      Name = "Figure0"+str(Nr)+".gif"
      self.Bild.append(PhotoImage(file="Bilder/"+Name))

  def showImage(self, x, y, Nr) :
    self.hideImage()
    self.Figure = self.Graphic.create_image(x, y, image=self.Bild[Nr])

  def moveImage(self, von, bis) :
    self.LR = -self.LR
    for pos in range(von, bis, 10) :
      self.step = 10 * self.LR
      if self.BildNr == 3 - self.LR :
        self.BildNr = 7 - self.LR
      else :
        self.BildNr = 3 - self.LR
      self.Graphic.itemconfig(self.Figure, image=self.Bild[self.BildNr])
      self.x, self.y = self.Graphic.coords(self.Figure)    
      if (self.x >= von+100) and (self.x <= bis+100) :
        self.Graphic.move(self.Figure, self.step, 0)
        self.Graphic.update()
        self.Graphic.after(100)
    self.Graphic.move(self.Figure, -self.step, 0)
    self.Graphic.itemconfig(self.Figure, image=self.Bild[1])

  def turnImage(self) :
    for Nr in range(1, 5) :
      self.Graphic.itemconfig(self.Figure, image=self.Bild[Nr]) 
      self.Graphic.update()
      self.Graphic.after(200)
    self.Graphic.itemconfig(self.Figure, image=self.Bild[1])      
 
  def hideImage(self) :
    self.Graphic.delete(self.Figure)




