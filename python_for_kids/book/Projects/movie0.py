# Анимация
from tkinter import *

# Размеры окна и текста
Width = 500
Height = 330
Mode = ["Появление", "Движение", "Сокрытие"]

# Функция события
def showImage() :
  pass
def moveImage() :
  pass
def hideImage() :
  pass

# Основная программа
Window = Tk()
Window.title("Анимация")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
Button = []
for Nr in range(0,3) :
  Button.append(Button(Window, text=Mode[Nr]))
  Button[Nr].place(x=30+Nr*150, y=Height-50, width=140, height=30)
Button[0].config(command=showImage)
Button[1].config(command=moveImage)
Button[2].config(command=hideImage)
Window.mainloop()

