# Анимация
from tkinter import *
from mplayerY import *

# Режим и текст
Width, Height = 600, 400
x, y = 120, 160
Mode = ["Появление", "Движение", "Поворот", "Сокрытие"]

# Основная программа
Window = Tk()
Window.title("Анимация")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
# Игровой персонаж
Gameer = Player(Graphic)
# Управление
Button = []
for Nr in range(0,4) :
  Button.append(Button(Window, text=Mode[Nr]))
  Button[Nr].place(x=30+Nr*135, y=Height-50, width=130, height=30)
Button[0].config(command=lambda : Gameer.showImage(x,y,1))
Button[1].config(command=lambda : Gameer.moveImage(20,Width-200))
Button[2].config(command=Gameer.turnImage)
Button[3].config(command=Gameer.hideImage)
Window.mainloop()


