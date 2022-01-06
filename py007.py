#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
There is Analizator tool for log-files from Prismaflex (look for COMMUNICATION ERROR)
Dmytro Melnychenko had made this.
19-SEP-2021 is the first day
"""

##-- log analizer
##-- Dmytro Melnychenko AKA D-Man
##-- program name - ?




#-- libraries
import os
import sys
import threading
import tempfile
import shutil
import tarfile

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class LOX_Analizer(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        print(fname)
        print(os.path.dirname(fname))
        with open("hello.txt", "w") as file_result:
            file_result.writelines("First Line")
        print(file_result)

        fdirectory = os.path.dirname(fname)
        list_of_files = os.listdir(fdirectory)

        for file in list_of_files:
            print(file, "----------------------")

            # создаём временную директорию
            with tempfile.TemporaryDirectory() as directory:
                print('Создана временная директория %s' % directory)
                try:
                    shutil.copyfile(fname, os.path.join(directory, "log_file_packed"))
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
                
                # считываем все строки
                content = file.readlines()
                # известно, что первые 27 строк - общая информация, пропускаем их
                for i in range(27): content.pop(0)

                # записать в переменную время начала сеанса
                therapy_start = (content[0].strip().split(";"))[1]
                
                # поиск вхождений искомого текста в строке
                for line in content:
                    # разбить строку на элементы
                    element = (line.strip()).split(";")
                    # записать в переменную время завершения сеанса
                    therapy_finish = element[1]
                    if element[4] == '90' or element[4] == '91' or element[4] == '97' or element[4] == '93' or element[4] == '94' or element[4] == '95':
                        print(element, "   ", file_result)
                        #Запишем некоторую информацию в файл "hello.txt":
                        with open("hello.txt", "a") as file_result:
                            file_result.writelines(element)
                        #Если мы откроем папку, в которой находится текущий скрипт Python, то увидем там файл hello.txt.
                
                #datetime.strptime('2014-11-17 00:00:00', '%Y-%m-%d %H:%M:%S')
                """
                """
                
                print(therapy_start, " -- ", therapy_finish)

                output_text = therapy_start + " -- " + therapy_finish

                self.textEdit.setText(output_text)

                # закрываем файл
                file.close
        
        #file_result.close()



        """
        # создаём временную директорию
        with tempfile.TemporaryDirectory() as directory:
            print('Создана временная директория %s' % directory)
            try:
                shutil.copyfile(fname, os.path.join(directory, "log_file_packed"))
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
            
            # считываем все строки
            content = file.readlines()
            # известно, что первые 27 строк - общая информация, пропускаем их
            for i in range(27): content.pop(0)

            # записать в переменную время начала сеанса
            therapy_start = (content[0].strip().split(";"))[1]
            
            # поиск вхождений искомого текста в строке
            for line in content:
                # разбить строку на элементы
                element = (line.strip()).split(";")
                # записать в переменную время завершения сеанса
                therapy_finish = element[1]
                if element[4] == '90' or element[4] == '91':
                    print(element)
            
            #datetime.strptime('2014-11-17 00:00:00', '%Y-%m-%d %H:%M:%S')
            " ""
            Запишем некоторую информацию в файл "hello.txt":
            with open("hello.txt", "w") as file:
                file.write("hello world")
            Если мы откроем папку, в которой находится текущий скрипт Python, то увидем там файл hello.txt.
            " ""
            
            print(therapy_start, " -- ", therapy_finish)

            output_text = therapy_start + " -- " + therapy_finish

            self.textEdit.setText(output_text)

            # закрываем файл
            file.close
        """

        """
        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)
        """



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = LOX_Analizer()
    sys.exit(app.exec_())