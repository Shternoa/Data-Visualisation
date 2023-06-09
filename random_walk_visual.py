import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from random_walk import RandomWalk

while True:
    # Построенеи случайного блуждания с нанесением точек на диаграмму
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_point, rw.y_point, s=20)
    plt.show()

    running = input('Сделать ещё одно блуждание? (y/n): ')
    if running == 'n':
        break
