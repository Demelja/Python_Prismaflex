## threads - потоки ##
import time 
from threading import Thread
import random
import math
# !!! Импортируем один из пакетов Matplotlib
import pylab
# !!! Импортируем пакет со вспомогательными функциями
from matplotlib import mlab
# Исправить:
import numpy




# псевдоисточник сигнала: случайное дописывается в конец массива, тем самым выдавливая первое
# цикл через 1 мс(?)
def source(int_array):
    # smth
    for i in range(len(int_array)-1):
        int_array[i] = int_array[i+1]
    int_array[127] = random.randint(-5,5)



# визуализация - массив отображается графиком
# цикл через 1 мс(?)
def chart(xs, int_array):
    # smth
    # printing array 
    print(int_array)
    pylab.plot (xs, int_array)




# Будем рисовать график этой функции
#def func (x):
#    """
#    sinc (x)
#    """
#    if x == 0:
#        return 1.0
#    return math.sin (x) / x

# основная программа: запускает поток источника, через 1мс(?) запускает функцию визуализации
# creating list, size = 128
xs = []
int_array = []
for i in range(128):
    int_array.append(0)
    xs.append(i)

xlist = numpy.arange (0, 130, 1)

# Создаём новый поток
th = Thread(target=source, args=(int_array, ))
# И запускаем его
th.start()
for i in range(2):
    time.sleep(2)
    chart(xs, int_array)
th.join()

# Интервал изменения переменной по оси X
#xmin = -20.0
#xmax = 20.0

# Шаг между точками
#dx = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
##xlist = mlab.frange (xmin, xmax, dx)
#Исправить:
#xlist = numpy.arange (0, 130, 1)

# Вычислим значение функции в заданных точках
#ylist = [func (x) for x in xlist]

# !!! Нарисуем одномерный график
#pylab.plot (xs, int_array)

# !!! Покажем окно с нарисованным графиком
pylab.show()