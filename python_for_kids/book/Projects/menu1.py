from tkinter import *

def newFile():
  pass
def openFile():
  pass
def saveFile():
  pass

# Основная программа    
Window = Tk()
Menuitem = Menu(Window)
Window.config(menu=Menuitem)

Filemenu = Menu(Menuitem,tearoff = 0)
Menuitem.add_cascade(label="Файл", menu=Filemenu)
Filemenu.add_command(label="Создать", command=newFile)
Filemenu.add_command(label="Открыть", command=openFile)
Filemenu.add_command(label="Сохранить", command=saveFile)
Filemenu.add_command(label="Выход", command=Window.destroy)

Helpmenu = Menu(Menuitem,tearoff = 0)
Menuitem.add_cascade(label="Справка", menu=Helpmenu)
Helpmenu.add_command(label="О программе")

Window.mainloop()
