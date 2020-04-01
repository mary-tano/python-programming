# Графика
from tkinter import *

# Размеры окна
Width = 500
Height = 330

# Функция события
def buttonClick() :
  Graphic.create_rectangle(20, 20, Width-20, Height-20)
  Graphic.create_oval(20, 20, Width-20, Height-20)
  Graphic.create_line(Width/2, 20, Width/2, Height-20)
  Graphic.create_line(20, Height/2, Width-20, Height/2)

# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
Button = Button(Window, text="Давай посмотрим!", command=buttonClick)
Button.place(x=Width/2-60, y=Height/2-15, width=120, height=30)
Window.mainloop()

