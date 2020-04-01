# 0 - 100 %
from tkinter import *

# Константы текста
State = ["Ты сказал мне:", "Я говорю тебе:", "Диагноз:"]
Diagnose = []
Psychosis = []
Max = 0

def scaleValue(event) :
  Nr = Slider.get()
  Display.config(text=str(Nr))

# Основная программа
Window = Tk()
Window.title("Проценты")
Window.minsize(width=400, height=180)
Display = Label(Window, text="0", font=("Arial", 24))
Display.place(x=20, y=30, width=350, height=60)

Slider = Scale(Window, orient="horizontal", command=scaleValue)
Slider.config(from_=0, to=100, length=360, showvalue=0)
Slider.place(x=20, y=120)
Window.mainloop()

