import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from random_walk import RandomWalk

while True:
    # Построенеи случайного блуждания с нанесением точек на диаграмму
    rw = RandomWalk(5000)
    rw.fill_walk()
    # Область просмотра
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers_list = list(range(rw.num_points))
    plt.plot(rw.x_point, rw.y_point, c='purple', linewidth=3)

    # Выделение первой и последней точек.
    plt.scatter(0, 0, c='red', linewidth=30)
    plt.scatter(rw.x_point[-1], rw.y_point[-1], c='blue', linewidth=30)

    # Удаление осей
    # plt.axes().get_xaxis().set_visible(True)
    # plt.axes().get_yaxis().set_visible(True)
    plt.show()

    running = input('Сделать ещё одно блуждание? (y/n): ')
    if running == 'n':
        break
