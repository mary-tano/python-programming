# Анимация
from tkinter import *

# Размеры окна и текста
Width, Height = 600, 350
Mode = ["Появление", "Движение", "Сокрытие"]

# Размер и расположение объекта
x, y, z = 20, 50, 200

# Функция события
def showImage() :
  global Circle
  Circle = Graphic.create_oval(x, y, x+z, y+z, fill="red")
def moveImage() :
  global Circle
  for pos in range(20,Width-220,2) :
    Graphic.move(Circle, 2, 0)
    Graphic.update()
    Graphic.after(10)   
def hideImage() :
  global Circle
  Graphic.delete(Circle)

# Основная программа
Window = Tk()
Window.title("Анимация")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
Knob = []
for Nr in range(0,3) :
  Knob.append(Button(Window, text=Mode[Nr]))
  Knob[Nr].place(x=80+Nr*150, y=Height-50, width=140, height=30)
Knob[0].config(command=showImage)
Knob[1].config(command=moveImage)
Knob[2].config(command=hideImage)
Window.mainloop()

