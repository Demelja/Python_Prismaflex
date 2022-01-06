## threads - потоки ##
import time 
from threading import Thread
import random
#import math
# !!! Импортируем один из пакетов Matplotlib
#import pylab
# !!! Импортируем пакет со вспомогательными функциями
#from matplotlib import mlab
# Исправить:
#import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import math



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
def chart(int_array):
    # smth
    # printing array 
    print(int_array)




# Будем рисовать график этой функции
#def func (x):
#    """
#    sinc (x)
#    """
#    if x == 0:
#        return 1.0
#    return math.sin (x) / x

# основная программа: запускает поток источника, через 1мс(?) запускает функцию визуализации
import array 
# creating array, size = 128
int_array = array.array('i', [])
for i in range(128):
    int_array.append(0)
# Создаём новый поток
th = Thread(target=source, args=(int_array, ))
# И запускаем его
#th.start()
for i in range(2):
    time.sleep(2)
    chart(int_array)
#th.join()

# Интервал изменения переменной по оси X
#xmin = -20.0
#xmax = 20.0

# Шаг между точками
#dx = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
##xlist = mlab.frange (xmin, xmax, dx)
#Исправить:
#xlist = numpy.arange (xmin, xmax, dx)

# Вычислим значение функции в заданных точках
#ylist = [func (x) for x in xlist]

# !!! Нарисуем одномерный график
#pylab.plot (xlist, ylist)

# !!! Покажем окно с нарисованным графиком
#pylab.show()