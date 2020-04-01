# Разметка окна
from tkinter import *

class Dialog() :
  
  # Инициализация
  def __init__(self, Title) :
    self.Window = Tk()
    self.Window.title(Title)
    self.Window.config(width=260, height=120)
    self.Display = Label(self.Window, text="Как дела?")
    self.Display.place(x=50, y=20, width=160, height=30)
    self.Button1 = Button(self.Window, text="Хорошо", \
    command=self.button1Click)
    self.Button2 = Button(self.Window, text="Плохо", \
    command=self.button2Click)
    self.Button1.place(x=20, y=70, width=100, height=30)
    self.Button2.place(x=140, y=70, width=100, height=30)
    self.Window.mainloop()
    
  # Метод
  def button1Click(self) :
    self.Display.config(text="Это радует!")
  def button2Click(self) :
    self.Display.config(text="Это огорчает!")

# Основная программа
Window = Dialog("Привет")

