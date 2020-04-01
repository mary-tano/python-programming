# Графика в Python
from tkinter import *

# Размеры окна
Breadth = 500
Highness = 330

# Функция события
def buttonClick() :
  Graphic.create_rectangle(20, 20, Breadth-20, Highness-20)
  Graphic.create_oval(20, 20, Breadth-20, Highness-20)
  Graphic.create_line(Breadth/2, 20, Breadth/2, Highness-20)
  Graphic.create_line(20, Highness/2, Breadth-20, Highness/2)

# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Breadth, height=Highness)
Graphic = Canvas(Window, width=Breadth, height=Highness)
Graphic.pack()
Button = Button(Window, text="Посмотреть!", command=buttonClick)
Button.place(x=Breadth/2-60, y=Highness/2-15, width=120, height=30)
Window.mainloop()

