# Гороскоп с кнопками
from tkinter import *

# Функция для события
# Здесь ты должен вставить свои собственные прогнозы!!!
def button1Click() :
  Display.config(text="Январь")
def button2Click() :
  Display.config(text="Февраль")
def button3Click() :
  Display.config(text="Март")
def button4Click() :
  Display.config(text="Апрель")
def button5Click() :
  Display.config(text="Май")
def button6Click() :
  Display.config(text="Июнь")
def button7Click() :
  Display.config(text="Июль")
def button8Click() :
  Display.config(text="Август")
def button9Click() :
  Display.config(text="Сентябрь")
def button10Click() :
  Display.config(text="Октябрь")
def button11Click() :
  Display.config(text="Ноябрь")
def button12Click() :
  Display.config(text="Декабрь")

# Основная программа
Window = Tk()
Window.title("Гороскоп")
Window.config(width=300, height=300)
Display = Label(Window, text="Твой  знак зодиака:")
Display.place(x=70, y=10, width=160, height=30)
# Знак зодиака
Button1  = Button(Window, text="Козерог", command=button1Click)
Button2  = Button(Window, text="Водолей", command=button2Click)
Button3  = Button(Window, text="Рыбы", command=button3Click)
Button4  = Button(Window, text="Овен", command=button4Click)
Button5  = Button(Window, text="Телец", command=button5Click)
Button6  = Button(Window, text="Близнецы", command=button6Click)
Button7  = Button(Window, text="Рак", command=button7Click)
Button8  = Button(Window, text="Лев", command=button8Click)
Button9  = Button(Window, text="Дева", command=button9Click)
Button10 = Button(Window, text="Весы", command=button10Click)
Button11 = Button(Window, text="Скорпион", command=button11Click)
Button12 = Button(Window, text="Стрелец", command=button12Click)
Button1.place(x=20, y=50, width=120, height=30)
Button2.place(x=160, y=50, width=120, height=30)
Button3.place(x=20, y=90, width=120, height=30)
Button4.place(x=160, y=90, width=120, height=30)
Button5.place(x=20, y=130, width=120, height=30)
Button6.place(x=160, y=130, width=120, height=30)
Button7.place(x=20, y=170, width=120, height=30)
Button8.place(x=160, y=170, width=120, height=30)
Button9.place(x=20, y=210, width=120, height=30)
Button10.place(x=160, y=210, width=120, height=30)
Button11.place(x=20, y=250, width=120, height=30)
Button12.place(x=160, y=250, width=120, height=30)
Window.mainloop()

