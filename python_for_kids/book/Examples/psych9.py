# Психолог
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import random

# Константы текста
State = ["Ты сказал мне:", "Я говорю тебе:", "Диагноз:"]
Diagnose = []
Psychosis = []
Max = 0

# Функции менюen
def initMenu() :
  Menuitem = Menu(Window)
  Window.config(menu=Menuitem)
  Filemenu = Menu(Menuitem, tearoff = 0)
  Menuitem.add_cascade(label="Файл", menu=Filemenu)
  #--
  Filemenu.add_command(label="Открыть", command=openFile, accelerator="Ctrl+O")
  Filemenu.add_command(label="Сохранить", command=saveFile, accelerator="Ctrl+S")
  Filemenu.add_command(label="Выход", command=closeAll, accelerator="Ctrl+X")
  Helpmenu = Menu(Menuitem, tearoff = 0)
  Menuitem.add_cascade(label="Справка", menu=Helpmenu)
  Helpmenu.add_command(label="О программе", command=showInfo)
def initPopup() :
  global ContextMenu
  ContextMenu = Menu(Window, tearoff = 0)
  ContextMenu.add_command(label="Открыть", command=openFile)
  ContextMenu.add_command(label="Сохранить", command=saveFile)
  ContextMenu.add_command(label="Выход", command=closeAll)
def openMenu(event):
  global ContextMenu
  ContextMenu.post(event.x_root, event.y_root)

# Файловые функции
def loadDiagnose(Name) :
  global Max
  Nr = 0
  try :
    File = open(Name, "r")
    for String in File :
      Diagnose.append(String.rstrip())
      Nr += 1
    Max = Nr - 1
    File.close()
  except :
    Diagnose.append("Что-то не так с файлом диагнозов")
def saveDiagnose(Name) :
  try :
    File = open(Name, "w")
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
  saveDiagnose("psychoX.txt") 
def scaleValue(event) :
  Nr = Slider.get()
  Answer.config(text=Diagnose[Nr])

# Команды меню
def openFile() :
  Name = filedialog.askopenfilename(filetypes= \
         (("Текстовые файлы","*.txt"),("Все файлы","*.*")))
  if Name != "" :
    Diagnose.clear()
    loadDiagnose(Name)
    Slider.config(to=Max) 
def saveFile() :
  Name = filedialog.asksaveasfilename()
  if Name != "" :
    saveDiagnose(Name)
def closeAll() :
  if messagebox.askyesno("Выход", "Сохранить данные?") :
    saveDiagnose("backup.txt") 
  Window.destroy()
def showInfo() :
  messagebox.showinfo("О программе", "Персональный психолог")

# События для клавиш
def getShotcut(event) :
  if event.keysym == "o" :
    openFile()
  if event.keysym == "s" :
    saveFile()
  if event.keysym == "x" :
    closeAll()

# Основная программа
Window = Tk()
Window.title("Психолог")
Window.minsize(width=500, height=330)
initMenu()
initPopup()
loadDiagnose("diagnose.txt")

# События
Window.bind("<Button-3>", openMenu)
Window.bind('<Control-o>', getShotcut)
Window.bind('<Control-s>', getShotcut)
Window.bind('<Control-x>', getShotcut)

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

# Завершение
Window.protocol("WM_DELETE_WINDOW", closeAll)

# Цикл событий
Window.mainloop()

