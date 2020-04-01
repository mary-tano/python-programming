# Окно
from tkinter import *

# Функция для события
def button1Click() :
  Display.config(text="Это радует!")
def button2Click() :
  Display.config(text="Это огорчает!")

# Основная программа
Window = Tk()
Display = Label(Window, text="Привет! Как дела?")
Display.config(font=("Tahoma",12,"normal"))
Display.pack()
Button1 = Button(Window, text="Хорошо", command=button1Click)
Button2 = Button(Window, text="Плохо", command=button2Click)
Button1.config(font=("Tahoma",12,"normal"))
Button2.config(font=("Tahoma",12,"normal"))
Button1.pack(side=LEFT)
Button2.pack(side=RIGHT)
Window.mainloop()
