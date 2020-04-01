# Словарь
from tkinter import *
import random

# Константы текста
Deutsch = []
English = []
Max = 0
Correct = -1

# Файловые функции
def loadDiagnose() :
  global Max
  Nr = 0
  XY = 1
  try :
    File = open("vokabeln.txt", "r")
    for String in File :
      Text = String.rstrip()
      if XY == 1 :
        Deutsch.append(Text)
      else :
        English.append(Text)
      XY = -XY
      Nr += 1
    Max = Nr/2 - 1
    File.close()
  except :
    Deutsch.append("Nichts")
    English.append("Nothing")

# Функция для события
def buttonClick() :
  global Correct
  Actual = random.randint(0,Max)
  Display.config(text=Deutsch[Actual])
  Maximum = random.randint(0,Max)
  Middle = random.randint(0,Max)
  Minimum = random.randint(0,Max)
  Correct = random.randint(0,2)
  Answer[0].config(text=English[Maximum])
  Answer[1].config(text=English[Middle])
  Answer[2].config(text=English[Minimum])
  Answer[Correct].config(text=English[Actual])
def getWord(Nr) :
  global Correct
  if Nr == Correct :
    Display.config(text="Правильно")
  else :
    Display.config(text="Неправильно")
    print(Nr)
  
# Основная программа
Window = Tk()
Window.title("Словарь")
Window.minsize(width=400, height=300)
loadDiagnose()

# Функции отображения и запросов
Display = Label(Window, text="Нажми Заново!")
Display.place(x=20, y=20, width=360, height=40)
Button = Button(Window, text="Заново", command=buttonClick)
Button.place(x=140, y=230, width=120, height=40)
Answer = []
for pos in range(0,3) :
  Answer.append(Button(Window, text="???"))
  Answer[pos].place(x=20, y=70+pos*50, width=360, height=40)
Answer[0].config(command=lambda: getWord(0))
Answer[1].config(command=lambda: getWord(1))
Answer[2].config(command=lambda: getWord(2))

# Цикл событий
Window.mainloop()

