#! /usr/bin/python

"""
Цикл лекций некоего Абглазова. Хорошо излагает
https://www.youtube.com/watch?v=9-6NkEK72pM
Попалось на глаза 15 марта 2021
"""

import threading
import time
import serial
import tkinter as tk

#-- глобальные переменные
in_list = []
out_flag = 0

#-- access to port: sudo chmod a+rw /dev/ttyUSB0
ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

#-- функция приема строки
def fn_in():
    global in_list
    while 1:
        in_len = 0
        while in_len < 1:
            in_st = ser.readline()
            in_len = len(in_st)
        in_list.append(in_st)
        time.sleep(1)

#-- запуск потока приема
tr_in = threading.Thread(target=fn_in)
tr_in.daemon = True
tr_in.start()

#-- функция
def fn_out():
    global out_flag
    out_flag = 1

#-- функция
def fn_send():
    out_st = ed.get()
    if len(out_st) > 0:
        ser.write(str.encode(out_st))
        lb.insert(tk.END, ">>> "+out_st)
    ed.delete(0, tk.END)

#-- функция вывода строк текста в листбокс
def fn_disp():
    global out_flag
    while len(in_list) > 0:
        st = in_list.pop(0)
        lb.insert(tk.END, st)
    if out_flag:
        fn_send()
        out_flag = 0
    root.after(100, fn_disp)

root = tk.Tk()
lb = tk.Listbox(root, width=20, height=5, font=('Calibri', 50))
lb.pack()
ed = tk.Entry(root, width=20, font=('Calibri', 50))
ed.pack()
bt = tk.Button(root, text="SEND", width=20, command=fn_out, font=('Calibri', 50))
bt.pack()
root.after(10,fn_disp)
root.mainloop()
