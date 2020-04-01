# Графика
from tkinter import *

# Функция события
def buttonClick() :
  pass

# Основная программа
Window = Tk()
Window.title("Графика")
Window.config(width=500, height=330)
Button = Button(Window, text="Давай посмотрим!", command=buttonClick)
Button.place(x=190, y=150, width=120, height=30)
Window.mainloop()

