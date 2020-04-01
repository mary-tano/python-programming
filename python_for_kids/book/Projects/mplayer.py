from tkinter import *

# Класс Player
class Player :
  Bild = [0]
  BildNr = 0
  
  def __init__(self, graphic) :
    self.Graphic = graphic
    for Nr in range(1,9) :
      Name = "Figure0"+str(Nr)+".gif"
      self.Bild.append(PhotoImage(file="Bilder/"+Name))

  def showImage(self, x, y, Nr) :
    self.Figure = self.Graphic.create_image(x, y, image=self.Bild[Nr]) 

  def moveImage(self, von, bis) :
    for pos in range(von, bis, 10) :
      if self.BildNr == 2 :
        self.BildNr = 6
      else :
        self.BildNr = 2
      self.Graphic.itemconfig(self.Figure, image=self.Bild[self.BildNr]) 
      self.Graphic.move(self.Figure, 10, 0)
      self.Graphic.update()
      self.Graphic.after(100)
    self.Graphic.itemconfig(self.Figure, image=self.Bild[1])      

  def hideImage(self) :
    elf.Graphic.delete(self.Figure)



