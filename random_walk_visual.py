import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from random_walk import RandomWalk

# Построенеи случайного блуждания с нанесением точек на диаграмму
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_point, rw.y_point, s=20)
plt.show()

