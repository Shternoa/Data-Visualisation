from random import randint


class Die():
    """Класс кубика"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Возвращает случайное число"""

        return randint(1, self.num_sides)
