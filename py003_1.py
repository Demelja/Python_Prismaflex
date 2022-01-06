## threads - потоки ##
import time 
from threading import Thread
import random
from matplotlib import pyplot
import numpy as np



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
    try:
        li.set_xdata([i for i in range(25)])
        li.set_ydata(int_array)
        pyplot.draw()
    except KeyboardInterrupt:
        pyplot.exit()
    pyplot.pause(0.011)




# основная программа: запускает поток источника, через 1мс(?) запускает функцию визуализации
int_array = [] * 128
pyplot.ion()
fig = pyplot.figure()
pyplot.title("Кажется, получается...")
ax1 = pyplot.axes()
li, = pyplot.plot(int_array)
pyplot.ylim([0,11])
# Создаём новый поток
th = Thread(target=source, args=(int_array, ))
# И запускаем его
th.start()

###
###for i in range(10):
    #time.sleep(0.5)
###    chart(int_array)
###
while True:
    try:
        li.set_xdata([i for i in range(25)])
        li.set_ydata(int_array)  # update the data
        pyplot.draw()  # update the plot
    except KeyboardInterrupt:
        pyplot.exit()
        break
    pyplot.pause(0.011)


th.join()
pyplot.ioff()
