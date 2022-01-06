#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Рассмотрим две функции из модуля filedialog – askopenfilename и asksaveasfilename. Первая предоставляет диалоговое окно для открытия файла, вторая – для сохранения. Обе возвращают имя файла, который должен быть открыт или сохранен, но сами они его не открывают и не сохраняют. Делать это уже надо программными средствами самого Python.

http://wummel.github.io/patool/
patool is a portable archive file manager
"""

"""
Как насчет использования tkinter?

from Tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

------------
tkFileDialog - диалоговое окно выбора файла
http://ilnurgi1.ru/docs/python/modules/tkFileDialog.html
------------
Ниже приведен пример сохранения пути каталога как глобальной переменной и использования этого для заполнения метки.

from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)

mainloop()
------------
Диалоговые (всплывающие) окна / tkinter 9
Обновлено: 04.10.2020
https://pythonru.com/uroki/dialogovye-vsplyvajushhie-okna-tkinter-9
------------
Как использовать Tkinter для открытия файла в папке с помощью раскрывающегося списка
https://quares.ru/?id=509006
------------
"""


from tkinter import *
from tkinter import filedialog as fd


def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()


def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

"""
root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=1, sticky=W)

root.mainloop()
"""


"""
 Используйте tkinter.filedialog в Python, чтобы открывать и сохранять изображения в формате диалога выбора файла.

tkinter.filedialog.asksaveasfilename () # Выберите имя файла для сохранения и верните имя файла
 tkinter.filedialog.askopenfilename () # Выберите файл для открытия и верните имя файла

Иногда мы хотим открыть изображение или сохранить изображение в формате диалогового окна выбора файла.После попытки я поделюсь с вами своим кодом для справки:
Откройте картинку и отобразите

root = tkinter.Tk () # Создать экземпляр Tkinter.Tk ()
root.withdraw () # скрыть экземпляр Tkinter.Tk ()
default_dir = r "путь к файлу"
file_path = tkinter.filedialog.askopenfilename (title = u 'выбрать файл', initialdir = (os.path.expanduser (default_dir)))
image = Image.open(file_path)
plt.imshow(image)
plt.show()

Сохранить картинку

fname = tkinter.filedialog.asksaveasfilename (title = u'save file ', filetypes = [("PNG", ".png")])
picture.save(str(fname) + '.png', 'PNG')

Просто выберите место сохранения после всплывающего диалогового окна и введите имя изображения.


[Примечание] Если следующие две строки кода не добавлены:

root = tkinter.Tk () # Создать экземпляр Tkinter.Tk ()
 root.withdraw () # скрыть экземпляр Tkinter.Tk ()


После запуска программы появится следующее маленькое окно:

"""


"""
Tkinter - самый простой способ, если вы не хотите иметь никаких других зависимостей. Чтобы показать только диалоговое окно без каких-либо других элементов графического интерфейса, вы должны скрыть корневое окно, используя withdraw метод:
"""
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
"""
"""
