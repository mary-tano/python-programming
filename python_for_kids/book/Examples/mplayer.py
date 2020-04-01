from tkinter import *

# Класс Player
class Player :
  Picture = [0]
  PictureNr = 0
  
  def __init__(self, graphic) :
    self.Graphic = graphic
    for Nr in range(1,9) :
      Name = "Figure0"+str(Nr)+".gif"
      self.Picture.append(PhotoImage(file="Bilder/"+Name))

  def showImage(self, x, y, Nr) :
    self.Figure = self.Graphic.create_image(x, y, image=self.Picture[Nr]) 

  def moveImage(self, von, bis) :
    for pos in range(von, bis, 10) :
      if self.PictureNr == 2 :
        self.PictureNr = 6
      else :
        self.PictureNr = 2
      self.Graphic.itemconfig(self.Figure, image=self.Picture[self.PictureNr]) 
      self.Graphic.move(self.Figure, 10, 0)
      self.Graphic.update()
      self.Graphic.after(100)
    self.Graphic.itemconfig(self.Figure, image=self.Picture[1])      

  def hideImage(self) :
    self.Graphic.delete(self.Figure)



