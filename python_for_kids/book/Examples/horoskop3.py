# Гороскоп со списком
from tkinter import *

# Здесь ты должен вставить свои собственные прогнозы!!!
Forecast = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", \
  "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
Zodiac = ["Козерог", "Водолей", "Рыбы", "Овен", "Телец", \
  "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец"]

# Функция события
def listboxSelect(event) :
  Select = Box.curselection()
  Nr = Select[0]
  Display.config(text=Forecast[Nr])
  

# Основная программа
Window = Tk()
Window.title("Гороскоп")
Window.minsize(width=300, height=400)
Display = Label(Window, text="Твой  знак зодиака:")
Display.place(x=40, y=10, width=160, height=30)

# Знак зодиака
Box = Listbox(Window)
for Nr in range(0,12) :
  Box.insert(Nr, Zodiac[Nr])
Box.bind("<<ListboxSelect>>", listboxSelect) 
Box.place(x=30,y=50, width=200, height=300)
  
# Цикл событий
Window.mainloop()

