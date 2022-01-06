## threads - потоки ##
import time 
from threading import Thread
import random
import math
# !!! Импортируем один из пакетов Matplotlib
from tkinter import *




# псевдоисточник сигнала: случайное дописывается в конец массива, тем самым выдавливая первое
# цикл через 1 мс(?)
def source(int_array):
    # smth
    while 1 == 1:
        r = random.randint(1,10)
        int_array.append(r)
        int_array.pop(0)



# визуализация - массив отображается графиком
# цикл через 1 мс(?)
def chart(int_array, root):
    # smth
    # printing array 
    print(int_array)

    First_x = -500
    for i in range(128):
        try:
            x = First_x + 8 * i
            y = int_array[i] * 60 - 300
            x += 500
            canv.create_oval(x, y, x + 1, y + 1, fill = 'black')
        except:
            pass
    canv.after(1, chart(int_array,root))




# основная программа: запускает поток источника, через 1мс(?) запускает функцию визуализации
import array 
# creating array, size = 128
int_array = array.array('i', [])
for i in range(128):
    int_array.append(0)
# new output window
#if __name__ == '__main__':
#    root = Tk()
root = Tk()
canv = Canvas(root, width = 1000, height = 1000, bg = "white")
canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
canv.create_line(0,500,1000,500,width=2,arrow=LAST)
canv.pack()	
## вызов ax.cla() удаляет (очищает) все что было нарисовано на ax.
# Создаём новый поток
th = Thread(target=source, args=(int_array, ))
# И запускаем его
th.start()

for i in range(10):
    #time.sleep(0.5)
    chart(int_array, root)

th.join()

root.mainloop()
