#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
There is ...
Dmytro Melnychenko had made this.
21-MAY-2021 is the first day
"""

##-- log analizer
##-- Dmytro Melnychenko AKA D-Man
##-- program name - ?




#-- libraries
import os
import threading
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import filedialog
from tkinter import Text
from tkinter import Label
from tkinter import Button
from tkinter import scrolledtext
from tkinter import Scrollbar
#from tkFont import Font
#import tkFileDialog
from sys import platform
import usb #pip install pyusb


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

##-- widget styles
###-- кнопка с набором параметров
class Buttongrid(ttk.Button):
    def __init__(self, panel, row_num, col_num, btn_text, btn_width=10, btn_fnc=""):
        ttk.Button.__init__(self, panel, text=btn_text, width=btn_width)
        self.grid(row=row_num, column=col_num, sticky="E"+"N", padx=5, pady=5)
        if btn_fnc != "":
            self.bind("<Button-1>", btn_fnc)

###--
class Radiobuttongrid(ttk.Radiobutton):
    def __init__(self, panel, row_num, col_num, radio_text, radio_width=15, radio_variable="", value=""):
        ttk.Radiobutton.__init__(self, panel, text=radio_text, width=radio_width, variable=radio_variable, value=value)
        self.grid(row=row_num, column=col_num, sticky="E"+"S", padx=10, pady=5)

###-- Textgrid



# open file explorer window
def fn_show_fileexplorer(event):
    file_name = filedialog.askopenfilename(filetypes = (("Archive files","*.LOX"),("all files","*.*")))
    dir_name = os.path.abspath(file_name+"/..")

    files = os.listdir(dir_name)
#    f = open(file_name)
#    s = f.read()
    scrollbar = Scrollbar(pnl_main)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    mylist = tk.Listbox(pnl_main, yscrollcommand = scrollbar.set )
    for eachfile in files:
        mylist.insert(tk.END, "Th " + eachfile)

    mylist.pack( side = tk.LEFT, fill = tk.BOTH )
    scrollbar.config( command = mylist.yview )

#    tex.insert(1.0, apparat.get())
#    tex.insert(1.0, s)
#    f.close()

def fn_show_explorer(event):
    file_name = filedialog.askopenfilename(filetypes = (("Archive files","*.LOX"),("all files","*.*")))
    dir_name = os.path.abspath(file_name+"/..")
    files = os.listdir(dir_name)
    lbl = Label(pnl_main, text="Привет++++")
    lbl_width = lbl.winfo_reqwidth()
    root.update()
    root_width = root.winfo_width()
    lbl_columns = root_width // lbl_width
    print(root_width, " // ", lbl_width, " = ", lbl_columns)
    rowu = 1
    colu = 1
    for eachfile in files:
        Label(pnl_main, text="Привет++++").grid(column=colu, row=rowu)
        colu=colu+1
        if colu>lbl_columns:
            colu=1
            rowu=rowu+1


'''
Вы можете указать начальную директорию для диалогового окна файла, указав initialdir следующим образом:

from os import path
file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
'''
'''
# open directory explorer window
def fnc_show_direxplorer(event):
    dir_name = filedialog.askdirectory()
    tex.insert(1.0, dir_name)
'''







#-- настройки оформления
root = tk.Tk()
#root.update_idletasks()

##-- control styles
clr_color = '#CDDE93'
stl = ttk.Style()
dFont = ('Helvetika', 10, 'bold')
stl.configure('.', font=dFont, background=clr_color, foreground='black')
stl.configure('TLabel', foreground='black', sticky="E", padx=10)
stl.configure('TButton', padx=5, pady=5, sticky="W", font=dFont)
stl.configure('TCombobox', padx=5, pady=5, sticky="W", width=10, font=dFont)

w = root.winfo_screenwidth() // 4
h = root.winfo_screenheight() // 4
root.geometry('+{}+{}'.format(w, h))

pnl_head = ttk.Frame(root,height=100)
pnl_main = ttk.Frame(root)
pnl_head.pack(fill="x")
pnl_main.pack(expand=1, fill="both")









apparat = StringVar()
apparat.set("PFX")
rad0 = Radiobuttongrid(pnl_head, 1, 1, u"Prismaflex", radio_variable=apparat, value="PFX")
rad1 = Radiobuttongrid(pnl_head, 1, 2, u"Prismax", radio_variable=apparat, value="PMX")
rad2 = Radiobuttongrid(pnl_head, 1, 3, u"AK98", radio_variable=apparat, value="AK98")

#lbl = Label(pnl_head, text="Привет+")
#print(lbl.winfo_reqwidth())

btn_fileexplorer = Buttongrid(pnl_head, 1, 4, u"Open HDD", 10, fn_show_explorer)

'''
###-- проверка операционной системы
if platform == "linux" or platform == "linux2":
    busses = usb.busses()
    for bus in busses:
        devices = bus.devices
        i = 4
        txt = scrolledtext.ScrolledText(pnl_main, width=40, height=10)
        txt.grid(column=0, row=0)
        for dev in devices:
#            handle = dev.open()
            print("Device:", dev.filename)
#            print("  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor))
#            print("  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct))
            i=i+1
            btn_fileexplorer = Buttongrid(pnl_head, 1, i, u"Open "+str(dev.filename)+str(i), 10, fn_show_fileexplorer)
            txt.insert(1.0, dev.filename)
#elif platform == "darwin":
#    # OS X
else: # win32 or Windows
    import win32com.client
    wmi = win32com.client.GetObject ("winmgmts:")
    for usbn in wmi.InstancesOf ("Win32_USBHub"):
        i=i+1
        btn_fileexplorer = Buttongrid(pnl_head, 1, i, u"Open "+str(usbn.DeviceID)+str(i), 10, fn_show_fileexplorer)
'''


'''
tex = Text(pnl_main, width=400, font="Verdana 12", wrap=tk.WORD)
tex.insert(1.1, "Start")
tex.grid(row=1,column=1)
'''


"""
###-- проверка операционной системы
if platform == "linux" or platform == "linux2":
    ports = ['/dev/ttyUSB%s' %i for i in range (20)]
#elif platform == "darwin":
#    # OS X
else: # win32 or Windows
    ports = ['COM%s' %(i+1) for i in range (20)]
###--
com_speed = 9600
com_parity = "N"
com_stopbits = 1
com_bytesize = 8
ser = ""
add_0D = 0

###-- заголовок правой панели
ttk.Label(pnl_ctrl, text='параметры соединения').grid(row=row_num, column=0, columnspan=1)

###-- найти все СОМ-порты
lst_ports = []
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        lst_ports.append(port)
    except(OSError, serial.SerialException):
        pass
if len(lst_ports) > 0:
    com_port = lst_ports[0]
else:
    com_port = "Nothing!"
"""



"""
#-- главная функция
flg_execute = 0
step_num = 0
main_tau = 30
def main():
    global flg_execute
    global step_num
    global link_mode
    global lst_in
    global busy_lstin
    if link_mode == 1:
        if len(lst_in) > 0:
            while busy_lstin:      # - подождать освобождения порта
                sleep(0.001)
            busy_lstin = True      # - занять порт
            str_in = lst_in.pop(0)
            busy_lstin = False     # - освободить порт
            lbx_log.append("=>"+str_in)
    if flg_execute:
        step_tau = int(edt_step.get())
        step_count = 1 + step_tau / main_tau
        step_num += 1
        if step_num > step_count:
            fnc_step(0)
            step_num = 0
        ### -- перезапуск после задержки
        root.after(main_tau, main)

main()
"""


#-- ЗАПУСТИТЬ
#if __name__ == "__main__ ":
root.mainloop()



#-- конец - делу венец
