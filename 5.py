"""Внести изменения в созданные классы следующим образом:
b.	динамические свойства классов “Point” и “Time” должны иметь модификатор доступа protected;
c.	определить методы getter и setter для свойств с модификаторами доступа private и protected;
d.	любое взаимодействие с private и protected свойствами  должно производиться посредством соответствующих методов getter и setter.
	Продемонстрировать работу измененных классов.
"""

from math import sqrt
class Point:
    # статические свойства: количество точек, лежащих на оси X, количество точек, лежащих на оси Y,
    #  количество точек, совпадающих с началом координат
    ox_count = 0
    oy_count = 0
    oo_count = 0

    #конструктор: вызывает конструктор родительского класса и выводит
    # сообщение о создании новой точки
    def __new__(cls, *args, **kwargs):
        print('A new point was created!')
        return super().__new__(cls) # вызываем конструктор родит класса

    # инициализатор: определяет динамические свойства класса и выводит созданный объект на экран
    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)
        self.print_point()
        print("-" * 20)
        Point.add_point(x, y) # классовый метод, обращаемся через имя класса Point и добавляем метод

    # деструктор: выводит сообщение о том, что точка удалена
    def __del__(self):
        print(f'The point ({self.get_x()}, {self.get_y()}) was deleted.')

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    @classmethod
    def add_point(cls, x, y):
        if cls.is_start_point(x, y): # если стартовая точка, т.е. х=0 и у=0, т.е  def inc_oo_count(cls)
            cls.inc_oo_count()
        elif cls.lies_on_ox(y):
            cls.inc_ox_count()
        elif cls.lies_on_oy(x):
            cls.inc_oy_count()

    @classmethod
    def del_point(cls, x, y):
        if cls.is_start_point(x, y): # если стартовая точка, т.е. х=0 и у=0, т.е  def inc_oo_count(cls)
            cls.inc_oo_count(value=-1)
        elif cls.lies_on_ox(y):
            cls.inc_ox_count(value=-1)
        elif cls.lies_on_oy(x):
            cls.inc_oy_count(value=-1)

    #классовые методы: увеличить на 1 количество точек, лежащих на оси X, увеличить на 1 количество точек,
    #лежащих на оси Y, увеличить на 1 количество точек, совпадающих с началом координат
    @classmethod
    def inc_ox_count(cls, value = 1):
        cls.ox_count += value

    @classmethod
    def inc_oy_count(cls, value = 1):
        cls.oy_count += value

    @classmethod
    def inc_oo_count(cls, value = 1):
        cls.oo_count += value

    #статические методы: проверки, лежит ли точка на одной из осей координат или
    # совпадает с началом координат
    @staticmethod
    def is_start_point(x, y):  # совпадает с началом координат
        return x == 0 and y == 0

    @staticmethod
    def lies_on_ox(y):
        return y == 0 # если y = 0, значит точка лежит на оси ox

    @staticmethod
    def lies_on_oy(x):
        return x == 0

    # методы: перемещение точки по оси X
    def move_ox(self, x): # то значение на кот мы перемещаем заданную точку
        Point.del_point(self.get_x(), self.get_y())
        self.set_x(self.get_x() + x) # self.x += x
        Point.add_point(self.get_x(), self.get_y())

    # перемещение точки по оси Y
    def move_oy(self, y):
        Point.del_point(self.get_x(), self.get_y())
        self.set_y(self.get_y() + y) # self.y += y
        Point.add_point(self.get_x(), self.get_y())

    # определение расстояния до начала координат
    def dist_to_start_point(self):
        # v((x1-x2)^2 + (y1 -y2)^2), у нас начало координат значит x2 = 0 и y2 = 0
        d = sqrt(self.get_x() ** 2 + self.get_y() ** 2)
        print(f'The distance to the start point (0, 0) is: {d:.2f}')
        return d

    # вычисление расстояния до заданной точки v((x1-x2)^2 + (y1 -y2)^2)
    # тут нужно получить саму точку и тут нужно получить объект нашего класса, а не x, y
    def dist_to_point(self, point):
        x_len = self.get_x() - point.get_x()
        y_len = self.get_y() - point.get_y()
        d = sqrt(x_len**2 + y_len**2)
        print(f'The distance to the point ({point.get_x()}, {point.get_y()}) is: {d:.2f}')
        return d


    # сравнение на совпадение и несовпадение с заданной точкой
    def is_the_same_point(self, point):
        res = self.get_x() == point.get_x() and self.get_y() == point.get_y()  # если наш х совпадает с х заданной точки и e совпадает с у заданной точки
        print(f'The point {"coincides" if res else "does not coincide"} with the point ({point.get_x}, {point.get_y()})')
        return res

    # вывод точки на экран
    def print_point(self):
        print(f'The point is:({self.get_x()}, {self.get_y()})')

p = [Point(2, 6), Point(4, 6), Point(0, 3), Point(0, 0), Point(0, 12)]
print(f'Lies on OX: {Point.ox_count}')
print(f'Lies on OY: {Point.oy_count}')
print(f'Lies on OO: {Point.oo_count}')
print()

p[0].move_ox(5)
p[0].print_point()
p[0].move_oy(5)
p[0].print_point()
print()

p[0].move_ox(-7)
p[0].print_point()
p[1].move_oy(3)
p[2].move_ox(-3)
print(f'Lies on OX: {Point.ox_count}')
print(f'Lies on OY: {Point.oy_count}')
print(f'Lies on OO: {Point.oo_count}')

p[0].print_point()
p[0].dist_to_start_point()
p[0].dist_to_point(p[4])
print()

p[0].is_the_same_point(p[0])
p[0].is_the_same_point(p[1])
print()
