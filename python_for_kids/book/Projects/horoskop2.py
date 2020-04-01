# Гороскоп с кнопками
from tkinter import *

# Здесь ты должен вставить свои собственные прогнозы!!!
Forecast = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", \
  "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
Zodiac = ["Козерог", "Водолей", "Рыбы", "Овен", "Телец", \
  "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец"]

# Функция события
def buttonClick(Nr) :
  Display.config(text=Forecast[Nr])

# Основная программа
Window = Tk()
Window.title("Гороскоп")
Window.minsize(width=300, height=400)
Display = Label(Window, text="Твой  знак зодиака:")
Display.place(x=70, y=10, width=160, height=30)

# Знак зодиака
Star = []
for Nr in range(0,12) :            
  Star.append(Button(Window, text=Zodiac[Nr]))
for pos in range(0,6) :
  Star[pos].place(x=20, y=60+pos*40, width=120, height=30)
  Star[pos+6].place(x=160, y=60+pos*40, width=120, height=30)
  
# Индивидуальная настройка событий
Star[0].config(command=lambda: buttonClick(0))
Star[1].config(command=lambda: buttonClick(1))
Star[2].config(command=lambda: buttonClick(2))
Star[3].config(command=lambda: buttonClick(3))
Star[4].config(command=lambda: buttonClick(4))
Star[5].config(command=lambda: buttonClick(5))
Star[6].config(command=lambda: buttonClick(6))
Star[7].config(command=lambda: buttonClick(7))
Star[8].config(command=lambda: buttonClick(8))
Star[9].config(command=lambda: buttonClick(9))
Star[10].config(command=lambda: buttonClick(10))
Star[11].config(command=lambda: buttonClick(11))

# Цикл событий
Window.mainloop()

