# Психолог
from tkinter import *
import random

# Константы текста
State = ["Ты сказал мне:", "Я говорю тебе:", "Диагноз:"]
Diagnose = []
Psychosis = []
Max = 0

# Файловые функции
def loadDiagnose() :
  global Max
  Nr = 0
  try :
    File = open("diagnose.txt", "r")
    for String in File :
      Diagnose.append(String.rstrip())
      Nr += 1
    Max = Nr - 1
    File.close()
  except :
    Diagnose.append("Перерыв")
def saveDiagnose() :
  try :
    File = open("psychoX.txt", "w")
    for String in Psychosis :
      File.write(String+"\n")
    File.close()
  except :
    print("Не получается сохранить файл")  

# Функция для события
def button1Click() :
  Input.delete(0,"end")
  Answer.config(text="")
def button2Click() :
  Nr = random.randint(0,Max)
  Answer.config(text=Diagnose[Nr])
  Psychosis.append(Input.get())
  Psychosis.append(Diagnose[Nr])
  saveDiagnose()
  
def scaleValue(event) :
  Nr = Slider.get()
  Answer.config(text=Diagnose[Nr])

# Основная программа
Window = Tk()
Window.title("Психолог")
Window.minsize(width=500, height=330)
loadDiagnose()

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
Slider = Scale(Border[2], orient="horizontal", command=scaleValue)
Slider.config(from_=0, to=Max, length=430, showvalue=0)
Slider.pack(pady=10) 

# Кнопки "Готово" и "Заново"
Button1 = Button(Window, text="Заново", command=button1Click)
Button1.place(x=120, y=285, width=120, height=30)
Button2 = Button(Window, text="Готово", command=button2Click)
Button2.place(x=260, y=285, width=120, height=30)

# Цикл событий
Window.mainloop()

