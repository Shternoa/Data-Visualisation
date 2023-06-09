from random import choice


class RandomWalk():
    """ Генерация случайных блужданий"""

    def __init__(self, num_points=5000):
        """Инициализация блуждания"""
        self.num_points = num_points

        self.x_point = [0]
        self.y_point = [0]

    def fill_walk(self):
        """Вычесление всех точек блуждения"""
        while len(self.x_point) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # Отклонение от 0 в перемещении
            if x_step == 0 and y_step == 0:
                continue

            # Следующие значения
            next_x = self.x_point[-1] + x_step
            next_y = self.y_point[-1] + y_step

            self.x_point.append(next_x)
            self.y_point.append(next_y)

    def get_step(self):
        # Определение направления и длинны перемещения
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step
