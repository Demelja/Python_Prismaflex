#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Цикл лекций некоего Абглазова. Хорошо излагает
https://www.youtube.com/watch?v=9-6NkEK72pM
Попалось на глаза 15 марта 2021
Вот только Python v.2.7

https://younglinux.info/tkinter/grid

"""

##-- simple terminal
##-- author
##-- program name




#-- libraries
import time
import serial
import threading
import tkinter as tk
from tkinter import ttk
#from tkinter import filedialog
#from tkFont import Font
#import tkFileDialog
from sys import platform




#-- настройки оформления
root = tk.Tk() # объект верхнего уровня

##-- control styles
clr_color = '#CDDE93'
stl = ttk.Style()
dFont = ('Helvetika', 12, 'bold')
stl.configure('.', font=dFont, background=clr_color, foreground='black')
stl.configure('TLabel', foreground='black', sticky="E", padx=10)
stl.configure('TEntry', padx=5, pady=5, sticky="W", font=dFont)
stl.configure('TButton', padx=5, pady=5, sticky="W", font=dFont)
stl.configure('TCombobox', padx=5, pady=5, sticky="W", width=10, font=dFont)

##-- widget styles
###-- кнопка с набором параметров
class Buttongrid(ttk.Button):
    def __init__(self, panel, row_num, col_num, btn_text, btn_width=10, btn_fnc=""):
        ttk.Button.__init__(self, panel, text=btn_text, width=btn_width)
        self.grid(row=row_num, column=col_num, sticky="E"+"N", padx=5, pady=5)
        if btn_fnc != "":
            self.bind("<Button-1>", btn_fnc)

###-- поле ввода с меткой
class Labelentry(ttk.Entry):
    def __init__(self, panel, row_num, col_num, lab_text="",
                ent_width=10, init_val="",
                fnc_return="", col_span=1):
        self.var = tk.StringVar()
        ttk.Entry.__init__(self, panel, width=ent_width, textvariable=self.var, font=dFont)
        self.var.set(init_val)
        if fnc_return != "":
            self.bind('Return'. fnc_return)

        if len(lab_text) > 0:
            self.lab = ttk.Label(panel, text=lab_text, font=dFont)
            self.lab.grid(row=row_num, column=col_num, sticky="E", padx=5)
        self.grid(row=row_num, column=col_num+1, columnspan=col_span, sticky="W", padx=5, pady=5)

    def get(self):
        return self.var.get()

    def set(self, new_text):
        self.var.set(new_text)

###-- поле чекбокса с меткой
class Labelcheckbutton(ttk.Checkbutton):
    def __init__(self, panel, row_num, col_num, lab_text="",
                ent_width=0, init_val=0,
                fnc_cmd="", col_span=1):
        self.var = tk.IntVar()
        self.var.set(init_val)
        if ent_width == 0:
            ent_width = len(lab_text)
        ttk.Checkbutton.__init__(self, panel, width=ent_width, variable=self.var, text=lab_text, command=fnc_cmd)
#        self.var.set(init_val)

        self.grid(row=row_num, column=col_num, sticky="E", padx=5, pady=5)

    def get(self):
        return self.var.get()

    def set(self, new_text):
        self.var.set(new_text)

###-- раскрывающийся список с меткой
class Labelcombobox(ttk.Combobox):
    def __init__(self, panel, row_num, col_num, lab_text="",
                cbx_width=20, cbx_height=6,
                lst_values=[1,2,3],
                fnc_sel="", col_span=1):
        if len(lab_text) > 0:
            self.lab = ttk.Label(panel, text=lab_text, font=dFont)
            self.lab.grid(row=row_num, column=col_num, sticky="E", padx=5, columnspan=col_span)

        ttk.Combobox.__init__(self, panel, values=lst_values, width=cbx_width, height=cbx_height, text=lab_text, font=dFont)
        self.set(lst_values[0])
        self.grid(row=row_num, column=col_num+1, sticky="W", padx=5, pady=5)
        if fnc_sel != 0:
            self.bind("<<Combobox Selected!!!>>", fnc_sel)

    def load(self, file_name):
        if len(file_name) >= 1:
            self["values"] = []
            fhn = open(file_name)
            self["values"] = fhn.readlines()
            fhn.close()
            self.set(self["values"][0])

###-- список с меткой

class Labellistbox(tk.Listbox):
    def __init__(self, panel, row_num, col_num, lab_text="",
                lbx_width=20, lbx_height=6,
                lst_values=[1,2,3], init_val=0,
                fnc_dbl="", col_span=1):
        self.panel = ttk.Frame(panel)
        tk.Listbox.__init__(self, self.panel, width=lbx_width, height=lbx_height, font=dFont)
        if len(lab_text) > 0:
            self.lab = ttk.Label(panel, text=lab_text, font=dFont)
            self.lab.grid(row=row_num, column=col_num, sticky="W", padx=5, pady=5, columnspan=2)
        self.panel.grid(row=row_num+1, column=col_num, sticky="W", padx=5, pady=5)
        for str_lbx in lst_values:
            tk.Listbox.insert(self, tk.END, str_lbx)

        self.pack(side="left", fill="y")
        self.scbr = tk.Scrollbar(self.panel, orient="vertical")
        self.scbr.pack(side="right", fill="y")

        self.scbr.config(command=self.yview)
        self.config(yscrollcommand=self.scbr.set)

        if fnc_dbl != 0:
            self.bind("<<Double-Button-1>>", fnc_dbl)

    def append(self, new_text):
        tk.Listbox.insert(self, tk.END, new_text)
        tk.Listbox.yview(self, tk.END)

    def get(self):
        try:
            return tk.Listbox.get(self, self.curselection()[0])
        except:
            return()

    def get_index(self):
        try:
            return self.curselection()[0]
        except:
            return -1

    def set_index(self, insex):
        try:
            self.select_clear(0, "end")
            self.selection_set(index)
            self.see(index)
            self.activate(index)
            self.selection_anchor(index)
            return index
        except:
            return -1

    def clear(self):
        tk.Listbox.delete(self, 0, tk.END)

    def insert(self, new_text):
        sel_num = self.get_index()
        if sel_num >= 0:
            tk.Listbox.insert(self, sel_num, new_text)
        else:
            tk.Listbox.insert(self, tk.END, new_text)

    def delete(self):
        sel_num = self.get_index()
        if sel_num >= 0:
            tk.Listbox.delete(self, sel_num)

    def save(self, file_name):
        if len(file_name) >= 1:
            fhn = open(file_name, "w")
            lst = list(Listbox.get(self, 0, tk.END))
            lst.append("")
            fhn.write('\n'.join(lst))
            fhn.close()

    def load(self, file_name):
        if len(file_name) >= 1:
            fhn = open(file_name)
            lst_values = fhn.readlines()
            fhn.close()

            tk.Listbox.delete(self, 0, tk.END)
            for str_loc in lst_values:
                tk.Listbox.insert(self, tk.END, str_loc.strip())















#-- панель с заголовком
pnl_head = ttk.Frame(root, height=100)
pnl_head.pack(side='top', fill='x')

##-- program head
ttk.Label(pnl_head, text="Terminal by Author")
ttk.Label(pnl_head, text='').pack()




#-- панель для содержимого
pnl_main = ttk.Frame(root, height=800)
pnl_main.pack(side="bottom", fill="both", expand=1)











##-- left panel
pnl_left = ttk.Frame(pnl_main, width=800)
pnl_left.pack(side="left", fill="both", expand=1)

###-- tk.listbox Журнал связи
lst_log=['log']
lst_width = 60
def fnc_lbxlogdb(ev):
    edt_strout.set(lbx_log.get()[2:])
lbx_log = Labellistbox(pnl_left, 0, 0, u"Журнал связи", lbx_height=6, init_val=0, col_span=1)

###-- поле ввода отправляемой строки
row_num = 16
def fnc_sendstrout(ev):
    global ser
    global add_0D
    if type(ser) == str: # обработать ошибку
        lbx_log.append(" ошибка: включите СОМ-порт")
        return

    loc_str = edt_strout.get() # записать строку
    str_out = loc_str.split(';'[0].strip()) # отрезать комментарии
    str_out = str_out.encode('utf8')

    if len(str_out) < 1: # отработать комментарий - нечего посылать
        lbx_log.append(" "+loc_str)
        return

    lbx_log.append("<="+loc_str) # подготовить строку к отправке
    if add_0D:
        str_out += "\r"
    str_out += "\n"
    ser.write(str_out)

edt_strout =Labelentry(pnl_left, row_num, 0, u"Строка:", lst_width-15, 'AT', fnc_return="", col_span=1)

###-- кнопка очистки поля ввода строки
row_num += 1
def fnc_clearout(event):
    edt_strout.set('')
btn_clearout = Buttongrid(pnl_left, row_num, 1, u"Clear it", 10, fnc_clearout)

###-- кнопка отправки
btn_sendout = Buttongrid(pnl_left, row_num, 3, u"отправить", 10, fnc_sendstrout)

###-- tk.listbox запомненных значений (программа)
row_num += 1
hgt_frmlbx = 8
lst_prog = ['AT', 'ATE0']
def fnc_lbxdbl(ev):
    edt_strout.set(lbx_prog.get())
    fnc_sendstrout(ev)
lbx_prog = Labellistbox(pnl_left, row_num, 0, u"список строк", lst_width, 8, lst_prog, fnc_lbxdbl, hgt_frmlbx, 4)

###-- кнопка очистки списка
row_num = row_num + 1 + hgt_frmlbx
def fnc_clearlstout(event):
    lbx_prog.clear()
btn_clearlbxout = Buttongrid(pnl_left, row_num, 0, u"очистить", 10, fnc_clearlstout)

###-- кнопка удаления строки из листбокса программы
def fnc_dellstout(event):
    lbx_prog.delete()
btn_dellbxout = Buttongrid(pnl_left, row_num, 0, u"удалить", 10, fnc_dellstout)

###-- кнопка вставки строки в листбокс
def fnc_inslbxout(event):
    lbx_prog.insert(edt_strout.get())
btn_inslbxout = Buttongrid(pnl_left, row_num, 2, u"вставить", 10, fnc_inslbxout)

###-- кнопка добавления строки в листбокс
row_num = 1 + hgt_frmlbx
def fnc_addlbxout(event):
    lbx_prog.append(edt_strout.get())
btn_addlbxout = Buttongrid(pnl_left, row_num, 3, u"Добавить", 10, fnc_addlbxout)

###-- кнопка: запись программы в файл
row_num += 1
def fnc_save(event):
    file_name = tkFileDialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if file_name != "":
        if file_name[-4:] != ".txt":
            file_name += ".txt"
        lbx_prog.save(file_name)
btn_save = Buttongrid(pnl_left, row_num, 2, u"записать", 10, fnc_save)

###-- кнопка: чтение программ из файла
def fnc_load(event):
    file_name = tkFileDialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
    if file_name != "":
        lbx_prog.load(file_name)
btn_load = Buttongrid(pnl_left, row_num, 3, u"прочитать", 10, fnc_load)










##-- right panel (control elements)
pnl_ctrl = ttk.Frame(pnl_main, width=100)
pnl_ctrl.pack(side='right', fill="y", padx=20)
row_num = 0

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

###-- комбобокс для выбора СОМ-порта
row_num += 1
def fn_cbxport(ev):
    global com_port
    com_port = cbx_port.get()
    fn_portoff(ev)
cbx_port = Labelcombobox(pnl_ctrl, row_num, 0, u"порт:", 10, 1, lst_ports, fn_cbxport)

###-- список значений скорости и комбобокс для ее выбора
row_num += 1
lst_comspeed = ['1200', '2400', '4800', '9600', '14400', '19200', '38400', '57600', '115200']
def fn_cbxspeed(ev):
    global com_speed
    com_speed = int(cbx_speed.get())
    fn_portoff(ev)
cbx_speed = Labelcombobox(pnl_ctrl, row_num, 0, u"скорость:", 10, 1, lst_comspeed, fn_cbxspeed)
cbx_speed.set(str(com_speed))

###-- комбобокс для выбора длины слова
row_num += 1
def fn_cbxwordlen(ev):
    global com_bytesize
    com_bytesize = int(cbx_wordlen.get())
    fn_portoff(ev)
cbx_wordlen = Labelcombobox(pnl_ctrl, row_num, 0, u"длина слова:", 10, 1, [5, 7, 8], fn_cbxwordlen)
#cbx_wordlen.set(str(com_bytesize))
cbx_wordlen.set(str("8"))

###-- комбобокс выбора проверки на четность
row_num += 1
def fn_cbxparity(ev):
    global com_parity
    parity = cbx_parity.get()
    dict_parity = {u"нет":"N", u"чётно":"E", u"нечет":"O"}
    com_parity = dict_parity[parity]
    fn_portoff(ev)
cbx_parity = Labelcombobox(pnl_ctrl, row_num, 0, u"чётность:", 10, 1, ["нет","чётно","нечет"], fn_cbxparity)
cbx_parity.set("нет")

###-- комбобокс выбора стоп-битов
row_num += 1
def fn_cbxstopbits(ev):
    global com_stopbits
    com_stopbits = int(cbx_stopbits.get())
    fn_portoff(ev)
cbx_stopbits = Labelcombobox(pnl_ctrl, row_num, 0, u"стоп.биты:", 10, 1, ["1", "2"], fn_cbxstopbits)
cbx_stopbits.set("1")

###-- чекбокс добавить 0x0D
row_num += 1
def fn_add0D():
    global add_0D
    add_0D = cbt_add0D.get()
cbt_add0D = Labelcheckbutton(pnl_ctrl, row_num, 0, u"добавить 0x0D", 12, 0, fn_add0D)
add_0D = 0
cbt_add0D.set(add_0D)

###-- строка активности СОМ-порта
row_num += 1
edt_mode = Labelentry(pnl_ctrl, row_num, 0, u"COM-порт:", 12, "отключён")

###-- кнопка отключить СОМ-порт
row_num += 1
link_mode = 0
def fn_portoff(ev):
    global link_mode
    global ser
    if link_mode == 1:
        try:
            ser.close()
            link_mode = 0
            edt_mode.set("отключён")
        except(OSError, serial.SerialException):
            edt_mode.set("ошибка")
btn_portoff = Buttongrid(pnl_ctrl, row_num, 0, u"отключить", 10, fn_portoff)
def fn_porton(ev):
    global link_mode
    global ser
    if link_mode==0:
        try:
            ser.close()
        except:
            pass
        try:
            ser = serial.Serial(port=com_port, baudrate=com_speed, parity=com_parity, stopbits=com_stopbits, bytesize=com_bytesize, timeout=0.010)
            link_mode = 1
            edt_mode.set("включён")
        except(OSError, serial.SerialException):
            edt_mode.set("ошибка")
btn_porton = Buttongrid(pnl_ctrl, row_num, 1, u"включить", 10, fn_porton)

###-- промежуток по строкам до поля длительности шага
for num in range(9):
    row_num += 1
    ttk.Label(pnl_ctrl, text="").grid(row=row_num, column=0)

###-- поле длительности шага
row_num += 1
edt_step = Labelentry(pnl_ctrl, row_num, 0, u"шаг(мс):", 6, "500")

###-- кнопка шага для листбокса программы (клик по строке в окне)
row_num += 1
def fnc_step(ev):
    global flg_execute
    index = lbx_prog.get_index()
    str_prog = lbx_prog.get().strip()
    if len(str_prog) > 2:
        if str_prog[0] != ";":
            edt_strout.set(str_prog)
            fnc_sendstrout(ev)
        index += 1
        lbx_prog.set_index(index)
    else:
        flg_execute = 0
btn_step = Buttongrid(pnl_ctrl, row_num, 0, u"выполнить", 10, fnc_step)

###-- кнопка запуска и останова непрерывного выполнения
def fnc_start(ev):
    global flg_execute
    if flg_execute == 0:
        flg_execute = 1
    else:
        flg_execute = 0
btn_start = Buttongrid(pnl_ctrl, row_num, 0, u"старт", 10, fnc_start)

















#-- поток приема из СОМ-порта
##-- функция приема сообщений
"""
def work_in():
    global lst_in
    global busy_in
    global ser
    global busy_ser
    while True:
        if not busy_ser:
            busy_ser = 1
            str_in = ser.readline()
            busy_ser = 0
            if len(str_in) > 0:
                while busy_in:
                    sleep(0.001)
                busy_in = 1
                str_in = str_in.strip()
                lst_in.append(str_in)
                busy_in = 0
                print "in: ", str_in
        sleep(0.001)
"""
lst_in = []
busy_lstin = False
def fnc_readport():
    global lst_in
    global busy_lstin
    global ser
    global link_mode
    while True:
        if link_mode == 1:
            try:
                str_in = str_in.strip()
                if len(str_in) > 1:
                    while busy_lstin:      # - подождать освобождения порта
                        sleep(0.001)
                    busy_lstin = True      # - занять порт
                    lst_in.append(str_in)  # - добавить строку
                    busy_lstin = False     # - освободить порт
            except:
                pass
        sleep(0.001)

##-- поток приема
"""
tr_in = threadin.Thread(target=work_in)
tr_in.daemon = True
tr_in.start()
"""
'''
tr_read = threading.Thread(target=fnc_readport)
tr_read.daemon = True
tr_read.start()
'''
##-- функция отправки сообщения
"""
def work_out():
    global lst_out
    global busy_out
    global ser
    global busy_ser
    while True:
        if len(lst_out)>0 and not busy_out and not busy_ser:
            busy_ser = 2
            busy_out = 2
            str_out = lst_out.pop(0)
            busy_out = 0
            str_out += "\ n" # <<<<<<<<<<<<<<<<<< !!!!!!!!
            busy_ser = 0
            print "out: ", str_out
        sleep(0.001)
"""

##-- поток отправки
"""
tr_out = threadin.Thread(target=work_out)
tr_out.daemon = True
tr_out.start()
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



#-- ЗАПУСТИТЬ
#if __name__ == "__main__ ":
root.mainloop()



#-- конец - делу венец
