from tkinter import *

Window = Tk()
Menuitem = Menu(Window)
Window.config(menu=Menuitem)

Filemenu = Menu(Menuitem)
Menuitem.add_cascade(label="Файл", menu=Filemenu)
Filemenu.add_command(label="Открыть")
Filemenu.add_command(label="Сохранить")
Filemenu.add_command(label="Выход")

Helpmenu = Menu(Menuitem)
Menuitem.add_cascade(label="Справка", menu=Helpmenu)
Helpmenu.add_command(label="О программе")

Window.mainloop()
