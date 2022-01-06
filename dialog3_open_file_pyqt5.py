#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
There is Analizator / Visualization tool for log-files from Prismaflex (soon - Prismax)
Dmytro Melnychenko had made this.
21-MAY-2021 is the first day
29-AUG-2021 jest drugir podejścia
"""

##-- log analizer
##-- Dmytro Melnychenko AKA D-Man
##-- program name - ?




#-- libraries
import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QDesktopWidget, QApplication)
import threading
import tempfile
import shutil
import tarfile


#-- настройки оформления - определения классов элементов
##-- control styles
###-- кнопка с набором параметров
class Buttongrid(QPushButton):
    def __init__(self, row_num, col_num, btn_text, btn_width=10, btn_fnc=""):
        QPushButton.__init__(self, text=btn_text, width=btn_width)
        self.grid(row=row_num, column=col_num, sticky="E"+"N", padx=5, pady=5)
        if btn_fnc != "":
            self.bind("<Button-1>", btn_fnc)

###-- graphic button
class ButtonGraphic(Buttongrid):
    def __init__(self, btn_pict):
        Buttongrid().__init__()
        self.setIcon(QIcon(file=os.path.abspath(__file__+"/..")+"/prismax300.png"))
        #self.setIconSize(QSize(75, 75))


###-- main window
class AnalizerMainApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize( 800, 800 )
        self.centerWindow()
        self.setWindowTitle( "Analizator zapisów zdarzeń i działań" )
        
        #button1 = Buttongrid( 0, 0, "111" )
        button2 = QPushButton( "2" )
        button3 = QPushButton( "З" )

        '''
        #-- панель с заголовком окна программы
        buttonl = Buttongrid( " l " )
        button4 = QPushButton( " 4 " )

        grid = QGridLayout( )

        grid.addWidget(buttonl , 0 , 0 )
        grid.addWidget(button2 , 0 , 1 )
        grid.addWidget(buttonЗ , 1 , 0 )
        grid.addWidget(button4 , 1 , 1 )

        w.setLayout(grid)
        w.show()
        '''
        grid = QGridLayout( )

        grid.addWidget(button2 , 0 , 0 )
        grid.addWidget(button2 , 0 , 1 )
        grid.addWidget(button3 , 1 , 0 )
        grid.addWidget(button2 , 1 , 1 )

        self.setLayout(grid)
        self.show()

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

##-- widget styles



'''
1. The Main Window contains a program name, description, author name + a standard button "Open Directory" + graphic button(s) "USB-D" "USB-E" etc.
   Pressing any buttons shows the select-a-file dialog window (a file name text field isn't shown). When USB-named button(s) used the start directory is USB-drive root. For the system disk - start point is User's directory.

2. Selected directory content shows like a list of files: filename + date of creation + size. Sorted - newest on the top

3. Clicking on the file name starts processes:
   - check if a working directory exist. If not - create (root - \home or /User)
   - remove any files inside a working directory
   - un-pack the file of archive pointed to the working directory
   - open the file named "file.PLE", extract time-of-start and time-of-end information, calculate treatment duration
   - re-draw the file list: scroll the row selected at the top of program window, expand this row, make file name font size bigger, show additional information, change color of row background

4. Clicking again on the file name selected (or an additional button) starts:
   - scan PLE-file, extact number of alarms was activated at this session (store in array)
   - make a temporary table with dimensions: the first is treatment duration in seconds, the second is number of alarms + pumps + scales + I2C signals etc.
   - show treatment info like graphs, bars ... starting 30 sec before threatment finish
   * the alarms's row has navigation buttons - to last/next signal
   * scale buttons

'''


# open file explorer window
'''
def fn_show_fileexplorer(event):
    file_name = filedialog.askopenfilename(filetypes = (("Archive files","*.LOX"),("all files","*.*")))
    dir_name = os.path.abspath(file_name+"/..")

    files = os.listdir(dir_name)
#    f = open(file_name)
#    s = f.read()
    scrollbar = Scrollbar(pnl_main)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = tk.Listbox(pnl_main, yscrollcommand = scrollbar.set )
    for eachfile in files:
        mylist.insert(tk.END, "Th " + eachfile)

    mylist.pack( side = tk.LEFT, fill = tk.BOTH )
    scrollbar.config( command = mylist.yview )

#    tex.insert(1.0, apparat.get())
#    tex.insert(1.0, s)
#    f.close()
'''




# open file explorer window
'''
def fn_show_explorer():
    frm_frame.destroy()
    frm_list = Frame(root).grid(column=0, row=0)

    file_name = filedialog.askopenfilename(filetypes = (("Archive files","*.LOX"),("all files","*.*")))
    dir_name = os.path.abspath(file_name+"/..")

    lbl = Label(frm_list, text="088-88-8888, 88:880")
    lbl_width = lbl.winfo_reqwidth()
    root.update()
    root_width = root.winfo_width()
    lbl_columns = root_width // lbl_width
    rowu = 1
    colu = 2

    with os.scandir(dir_name) as listOfEntries:
        for entry in listOfEntries:
            # печать всех записей, являющихся файлами
            if entry.is_file():
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(entry)
#                print(f'os.stat({entry.name}):)
#                print('  Size:', size)
#                print('  Permissions:', oct(mode))
#                print('  Owner:', uid)
#                print('  Device:', dev)
#                print('  Created      :', time.ctime(ctime))
#                print('  Last modified:', time.ctime(mtime)) #.strftime("%d-%m-%Y")
#                print('  Last accessed:', time.ctime(atime))
#                lbl2 = Label(pnl_main, text=time.ctime(mtime)+"\r"+str(size))
                lbl2 = Button(frm_list, text=time.strftime("%Y-%m-%d, %H:%M", time.localtime(mtime))+"\r"+str(size))
                lbl2.bind('<Button-1>', lambda event: fn_data_prepare(entry))
                lbl2.grid(column=colu, row=rowu, padx=4, pady=3)
                colu=colu+1
                if colu>lbl_columns:
                    colu=1
                    rowu=rowu+1
    listOfEntries.close()
'''

# preparation data selected
'''
def fn_data_prepare(data_file):
    print(data_file.name)
#    w = root.winfo_screenwidth()
#    h = root.winfo_screenheight()
#    root.geometry('{}x{}+{}+{}'.format(w, h, 0, 0))
    """
    3. Clicking on the file name starts processes:
   - check if a working directory exist. If not - create (root - \home or /User)
   - remove any files inside a working directory
   - un-pack the file of archive pointed to the working directory
   - open the file named "file.PLE", extract time-of-start and time-of-end information, calculate treatment duration
   - re-draw the file list: scroll the row selected at the top of program window, expand this row, make file name font size bigger, show additional information, change color of row background

4. Clicking again on the file name selected (or an additional button) starts:
   - scan PLE-file, extact number of alarms was activated at this session (store in array)
   - make a temporary table with dimensions: the first is treatment duration in seconds, the second is number of alarms + pumps + scales + I2C signals etc.
   - show treatment info like graphs, bars ... starting 30 sec before threatment finish
   * the alarms's row has navigation buttons - to last/next signal
   * scale buttons
    """
    """
    # вывести текущую директорию
    print("Текущая деректория:", os.getcwd())
    if os.path.isdir("tmp_data"):
        # удалить папку
            try:
                os.rmdir("tmp_data")
            except OSError:
                print ("Удалить директорию %s не удалось" % "tmp_data")
            else:
                print ("Успешно удалена директория %s " % "tmp_data")
    try:
        os.mkdir("tmp_data")
    except OSError:
        print ("Создать директорию %s не удалось" % "tmp_data")
    else:
        print ("Успешно создана директория %s " % "tmp_data")
        # изменение текущего каталога на 'folder'
        # os.chdir("tmp_data")
    """
    # создаём временную директорию
    with tempfile.TemporaryDirectory() as directory:
        print('Создана временная директория %s' % directory)
        try:
            shutil.copyfile(data_file, os.path.join(directory, "log_file_packed"))
        except IOError:
            print("Copy failed")
        else:
            print("Copied!", str(os.path.join(directory, "log_file_packed")))
        archive = tarfile.open(os.path.join(directory, "log_file_packed"), "r:gz")
        archive.extractall(directory)
        print("Extracted!", str(archive))
        print(os.listdir(path=directory))
        f_events = [f for f in os.listdir(path=directory) if f.endswith('.PLE')]
        print(f_events)
        file_data = f_events[0]
        print(file_data)
        # получим объект файла
        file = open(os.path.join(directory, file_data), mode="r", encoding="utf-16")
        while True:
            # считываем строку
            line = file.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            # выводим строку
            print(line.strip())
        # закрываем файл
        file.close
'''



#-- ЗАПУСТИТЬ
if __name__ == '__main__':
    app = QApplication(sys.argv)
    analizer = AnalizerAPI()
    sys.exit(app.exec_())









'''
root.title("Analizator zapisów zdarzeń i działań")

w = int(root.winfo_screenwidth() // 2)
h = int(root.winfo_screenheight() // 2)
x = int(root.winfo_screenwidth() // 4)
y = int(root.winfo_screenheight() // 4)
root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

root_width = root.winfo_width()

frm_frame = Frame(root)
frm_frame.pack(fill=BOTH, expand=True)

img_prismax = PhotoImage(file=os.path.abspath(__file__+"/..")+"/prismax300.png")
btn_prismax = Button(frm_frame, command=fn_show_explorer, image=img_prismax)
btn_prismax.pack(side = LEFT, expand = True, fill = BOTH, ipadx=8)

txt_declaration = Text(frm_frame, width=45)
txt_declaration.insert(1.0, "Clicking on the file name starts processes:    - check if a working directory exist. If not - create (root - \home or /User)    - remove any files inside a working directory    - un-pack the file of archive pointed to the working directory   - open the file named 'file.PLE', extract time-of-start and time-of-end information, calculate treatment duration   - re-draw the file list: scroll the row selected at the top of program window, expand this row, make file name font size bigger, show additional information, change color of row background")
txt_declaration.pack(side = LEFT, expand = True, fill = BOTH)

img_prismaflex = PhotoImage(file=os.path.abspath(__file__+"/..")+"/prismaflex300.png")
btn_prismaflex = Button(frm_frame, command=fn_show_explorer, image=img_prismaflex)
btn_prismaflex.pack(side = LEFT, expand = True, fill = BOTH, ipadx=8)

root.mainloop()
'''

#-- конец - делу венец
