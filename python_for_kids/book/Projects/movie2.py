# Анимация
from tkinter import *

# Режим и текст
Width, Height = 600, 400
x, y = 120, 160
Mode = ["Появление", "Движение", "Сокрытие"]

# Функция события
def showImage() :
  global Figure
  global Picture 
  Picture = PhotoImage(file="Bilder/Figure01.gif")
  Figure = Graphic.create_image(x, y, image=Picture) 
def moveImage() :
  global Figure
  for pos in range(20,Width-200,2) :
    Graphic.move(Figure, 2, 0)
    Graphic.update()
    Graphic.after(10)   
def hideImage() :
  global Figure
  Graphic.delete(Figure)

# Основная программа
Window = Tk()
Window.title("Анимация")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
Button = []
for Nr in range(0,3) :
  Button.append(Button(Window, text=Mode[Nr]))
  Button[Nr].place(x=80+Nr*150, y=Height-50, width=140, height=30)
Button[0].config(command=showImage)
Button[1].config(command=moveImage)
Button[2].config(command=hideImage)
Window.mainloop()


