"""2.	Создать класс “Pair” (пара чисел) со свойствами: числа A и B, - и методами:
изменение чисел, вычисление их произведения и суммы. Определить производный класс
“Right Triangle” (прямоугольный треугольник) со свойствами: катеты A и B, - и методами:
вычисление гипотенузы и площади треугольника, вывод информации о фигуре на экран.
Продемонстрировать работу класса-наследника и всех его методов."""

from math import sqrt

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def edit_A(self, a):
        self.a = a

    def edit_B(self, b):
        self.b = b

    def sum(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b

class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.c = self.hypot()

    def hypot(self): # перепишем init чтобы каждый раз в print_info не высчитывать гипотенузу для вывода
        hypot = round(sqrt(self.a**2 + self.b ** 2), 2)
        print(f'The hypotenuse of \u25B3ABC: {hypot}')
        return hypot
# так как в родительском класе мы можем изменять а и b, то и гипотенузу мы должны менять.
    # то есть мы должны переопределить эти методы в нашем классе потомке
    def edit_A(self, a):
        super().edit_A(a)
        self.c = self.hypot()

    def edit_B(self, b):
        super().edit_B(b)
        self.c = self.hypot()

    def square(self):
        # S = 1/2 * a * b
        s = round(1/2 * self.mult(), 2)
        print(f'The square of \u25B3ABC: {s}')
        return s

    def print_info(self):
        print(f'The right triangle \u25B3ABC ({self.a}, {self.b}, {self.c})')

tr = RightTriangle(5, 8)
tr.print_info()
tr.square()
print()

print(f'SUM: {tr.sum()}')
print(f'MULT: {tr.mult()}')

print()

tr.edit_A(10)
tr.edit_B(20)
print(f'SUM: {tr.sum()}')
print(f'MULT: {tr.mult()}')
tr.print_info()

