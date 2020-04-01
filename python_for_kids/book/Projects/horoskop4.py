# Гороскоп с переключателями
from tkinter import *

# Здесь ты должен вставить свои собственные прогнозы!!!
Forecast = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", \
  "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
Zodiac = ["Козерог", "Водолей", "Рыбы", "Овен", "Телец", \
  "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец"]

# Функция события
def buttonClick() :
  Display.config(text=Forecast[Nummer.get()]) 

# Основная программа
Window = Tk()
Window.title("Гороскоп")
Window.minsize(width=300, height=250)
Display = Label(Window, text="Твой  знак зодиака:")
Display.grid(row=0, column=0)

# Вспомогательные переменные
Nummer = IntVar()
Nummer.set(-1)

# Знак зодиака
Star = []
for Nr in range(0,12) :
  Star.append(Radiobutton(Window, variable=Nummer, value=Nr, text=Zodiac[Nr]))
  Star[Nr].config(command=buttonClick)
for pos in range(0,6) :
  Star[pos].grid(row=pos+1, column=0, sticky="w")
  Star[pos+6].grid(row=pos+1, column=1, sticky="w")
  
# Цикл событий
Window.mainloop()

