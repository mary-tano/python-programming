from tkinter import *

# Класс Player
class Player :
  Bild = [0]
  BildNr = 0
  Figure = 0
  
  def __init__(self, graphic) :
    self.Graphic = graphic
    for Nr in range(1,9) :
      Name = "Figure0"+str(Nr)+".gif"
      self.Bild.append(PhotoImage(file="Bilder/"+Name))

  def showImage(self, x, y, Nr) :
    self.hideImage()
    self.Figure = self.Graphic.create_image(x, y, image=self.Bild[Nr])

  def moveImage(self, von, bis) :
    for pos in range(von, bis, 10) :
      if self.BildNr == 2  :
        self.BildNr = 6
      else :
        self.BildNr = 2
      self.Graphic.itemconfig(self.Figure, image=self.Bild[self.BildNr])     
      self.x, self.y = self.Graphic.coords(self.Figure)    
      if self.x <= bis+100 :
        self.Graphic.move(self.Figure, 10, 0)
        self.Graphic.update()
        self.Graphic.after(100)
    self.Graphic.itemconfig(self.Figure, image=self.Bild[1])

  def turnImage(self) :
    for Nr in range(1, 5) :
      self.Graphic.itemconfig(self.Figure, image=self.Bild[Nr]) 
      self.Graphic.update()
      self.Graphic.after(200)
    self.Graphic.itemconfig(self.Figure, image=self.Bild[1])      
 
  def hideImage(self) :
    self.Graphic.delete(self.Figure)




