# Анимация
from tkinter import *
from mplayer import *

# Режим и текст
Width, Height = 600, 400
x, y = 120, 160
Mode = ["Появление", "Движение", "Сокрытие"]

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
for Nr in range(0,3) :
  Button.append(Button(Window, text=Mode[Nr]))
  Button[Nr].place(x=80+Nr*150, y=Height-50, width=140, height=30)
Button[0].config(command=lambda : Gameer.showImage(x,y,1))
Button[1].config(command=lambda : Gameer.moveImage(20,Width-200))
Button[2].config(command=Gameer.hideImage)
Window.mainloop()


