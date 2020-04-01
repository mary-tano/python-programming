# Анимация
from tkinter import *
from mplayerX import *

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
Knob = []
for Nr in range(0,4) :
  Knob.append(Button(Window, text=Mode[Nr]))
  Knob[Nr].place(x=30+Nr*135, y=Height-50, width=130, height=30)
Knob[0].config(command=lambda : Gameer.showImage(x,y,1))
Knob[1].config(command=lambda : Gameer.moveImage(20,Width-200))
Knob[2].config(command=Gameer.turnImage)
Knob[3].config(command=Gameer.hideImage)
Window.mainloop()


