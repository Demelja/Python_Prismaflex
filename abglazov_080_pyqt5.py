#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Цикл лекций некоего Абглазова. Хорошо излагает
https://www.youtube.com/watch?v=9-6NkEK72pM
Попалось на глаза 15 марта 2021
Моя трансляция на Python v.3.8 + PyQt5
"""

##-- simple terminal
##-- author
##-- program name




#-- libraries
import time
#import serial
import threading
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)



#-- настройки оформления - определения классов элементов
##-- control styles
##-- widget styles
###-- кнопка с набором параметров
class Buttongrid(QPushButton):
    def __init__(self, row_num, col_num, btn_text, btn_width=10, btn_fnc=""):
        QPushButton.__init__(self, text=btn_text, width=btn_width)
        self.grid(row=row_num, column=col_num, sticky="E"+"N", padx=5, pady=5)
        if btn_fnc != "":
            self.bind("<Button-1>", btn_fnc)


#-- панель с заголовком окна программы
#-- панель для содержимого
##-- левая панель
##-- правая панель

#-- Главное окно программы
app = QApplication(sys.argv)
w = QWidget()
w.resize(800, 800)
w.setWindowTitle("Простой терминал для связи через СОМ-порт")
#grid = QGridLayout()


#-- панель с заголовком окна программы
buttonl = QPushButton( " l " )
button2 = QPushButton( "2 " )
buttonЗ = QPushButton( " З " )
button4 = QPushButton( " 4 " )

grid = QGridLayout( )

grid.addWidget(buttonl , 0 , 0 )
grid.addWidget(button2 , 0 , 1 )
grid.addWidget(buttonЗ , 1 , 0 )
grid.addWidget(button4 , 1 , 1 )

w.setLayout(grid)
w.show()
sys.exit(app.exec_())

#-- Главная функция

#-- Запуск Главной функции
