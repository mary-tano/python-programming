from tkinter import *
from tkinter import filedialog

class MainMenu :
 
  def __init__(self, Window) :
    self.Window = Window
    Menuitem = Menu(self.Window)
    self.Window.config(menu=Menuitem)
    Filemenu = Menu(Menuitem, tearoff = 0)
    Menuitem.add_cascade(label="Файл", menu=Filemenu)
    Filemenu.add_command(label="Открыть", command=self.openFile)
    Filemenu.add_command(label="Сохранить", command=self.saveFile)
    Filemenu.add_command(label="Выход", command=self.closeAll)
    Helpmenu = Menu(Menuitem, tearoff = 0)
    Menuitem.add_cascade(label="Справка", menu=Helpmenu)
    Helpmenu.add_command(label="О программе")            

  def openFile(self) :
    self.File = filedialog.askopenfilename(filetypes= \
                 (("Текстовые файлы","*.txt"),("Все файлы","*.*")))   
  def saveFile(self) :
    self.File = filedialog.asksaveasfilename()
  def closeAll(self) :
    self.Window.quit()
    self.Window.destroy()
    
  def getName(self) :
    return self.File  


