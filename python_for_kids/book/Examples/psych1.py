# Психолог
from tkinter import *

# Константы текста
State = ["Ты сказал мне:", "Я говорю тебе:", "Диагноз:"]
Diagnose = ["Это здорово!", "Это радует!", "Все возможно.", \
            "Это огорчает!", "Это плохо!", "Раз ты так думаешь ..."]

# Функция для события
def button1Click() :
  pass
def button2Click() :
  pass
  
# Основная программа
Window = Tk()
Window.title("Психолог")
Window.minsize(width=500, height=330)

# Определение состояния
Display = []
Border = []
for pos in range(0,3) :
  Display.append(Label(Window, text=State[pos]))
  Display[pos].place(x=20, y=10+pos*90, width=460, height=30)
  Border.append(Frame(Window, borderwidth=2, relief="groove"))
  Border[pos].place(x=20, y=40+pos*90, width=460, height=50)

# Ввод, ответ и ползунковый регулятор
Input = Entry(Border[0])
Input.place(x=10, y=10, width=440, height=30)
Answer = Label(Border[1])
Answer.place(x=10, y=10, width=440, height=30)
Slider = Scale(Border[2], orient="horizontal")
Slider.config(length=430, showvalue=0)
Slider.pack(pady=10)

# Кнопки "Готово" и "Заново"
Button1 = Button(Window, text="Заново", command=button1Click)
Button1.place(x=120, y=285, width=120, height=30)
Button2 = Button(Window, text="Готово", command=button2Click)
Button2.place(x=260, y=285, width=120, height=30)

# Цикл событий
Window.mainloop()

