# Анимация
from tkinter import *

# Режим и текст
Width, Height = 600, 400
x, y = 120, 160
Mode = ["Появление", "Движение", "Сокрытие"]

# Класс Player
class Player :
  Picture = [0]
  def __init__(self, Graphic) :
    for Nr in range(1,9) :
      Name = "Figure0"+str(Nr)+".gif"
      self.Picture.append(PhotoImage(file="Bilder/"+Name))
  def showImage(self) :
    self.Figure = Graphic.create_image(x, y, image=self.Picture[1]) 
  def moveImage(self) :
    for pos in range(20,Width-200,2) :
      Graphic.move(self.Figure, 2, 0)
      Graphic.update()
      Graphic.after(10)   
  def hideImage(self) :
    Graphic.delete(self.Figure)

# Основная программа
Window = Tk()
Window.title("Анимация")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
# Игровой персонаж
Gameer = Player(Graphic)
# Управление
Knob = []
for Nr in range(0,3) :
  Knob.append(Button(Window, text=Mode[Nr]))
  Knob[Nr].place(x=80+Nr*150, y=Height-50, width=140, height=30)
Knob[0].config(command=Gameer.showImage)
Knob[1].config(command=Gameer.moveImage)
Knob[2].config(command=Gameer.hideImage)
Window.mainloop()


