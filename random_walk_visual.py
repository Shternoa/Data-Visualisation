import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from random_walk import RandomWalk

while True:
    # Построенеи случайного блуждания с нанесением точек на диаграмму
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers_list = list(range(rw.num_points))
    plt.scatter(rw.x_point, rw.y_point, c=point_numbers_list, cmap=plt.cm.Greens, edgecolors='none', s=1)

    # Выделение первой и последней точек.
    plt.scatter(0, 0, c='red', edgecolors='none', s=50)
    plt.scatter(rw.x_point[-1], rw.y_point[-1], c='blue', edgecolors='none', s=50)

    # Удаление осей
    # plt.axes().get_xaxis().set_visible(True)
    # plt.axes().get_yaxis().set_visible(True)
    plt.show()

    running = input('Сделать ещё одно блуждание? (y/n): ')
    if running == 'n':
        break
