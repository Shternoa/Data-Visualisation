import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from random_walk import RandomWalk

while True:
    # Построенеи случайного блуждания с нанесением точек на диаграмму
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers_list = list(range(rw.num_points))
    plt.scatter(rw.x_point, rw.y_point, c=point_numbers_list, cmap=plt.cm.Greens, edgecolors='none', s=12)
    plt.show()

    running = input('Сделать ещё одно блуждание? (y/n): ')
    if running == 'n':
        break
