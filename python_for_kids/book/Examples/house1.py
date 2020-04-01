# Дом
from tkinter import *

# Размеры окна
Width = 500
Height = 330

# Функция события
def buttonClick() :
  Graphic.create_rectangle(20, Height/2-20, Width-20, Height-20, fill="gray")
  Graphic.create_polygon((20, Height/2-20), (Width/2, 20), (Width-20, Height/2-20)) 
  # Дверь и окно
  Graphic.create_rectangle(50, Height/2+10, 150, Height/2+90, fill="blue")
  Graphic.create_rectangle(Width-50, Height/2+10, Width-150, Height/2+90, fill="blue")
  Graphic.create_rectangle(Width/2-40, Height/2+20, Width/2+40, Height-20, fill="brown")

# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=Width, height=Height)
Graphic = Canvas(Window, width=Width, height=Height)
Graphic.pack()
Button = Button(Window, text="Мой дом", bg="gray", command=buttonClick)
Button.place(x=Width/2-60, y=Height-45, width=120, height=30)
Window.mainloop()

