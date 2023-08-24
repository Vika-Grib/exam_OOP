"""3.	Внести изменения в созданный в первой задаче класс “Alcohol”:
переопределить методы вычисления массы и объема жидкости таким образом,
чтобы в них также рассчитывалось соответственно массовое или объемное содержание чистого спирта,
исходя из заданной крепости.
Переопределить метод вывода информации о спирте"""


class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def edit_density(self, val): #изменение плотности
        self.density = val

    def calc_v(self, m): # объем = масса/плотность
        v = round(m / self.density, 2)
        print(f'The volume of {m} kg of {self.name} is {v} m^3')
        return v

    def calc_m(self, v):
        m = v * self.density
        print(f'The weight of {v} m^3 of {self.name} is {m} kg.')
        return m

    def print_info(self):
        print(f'Liquid {self.name!r} (density = {self.density} kg/m^3).')

class Alcohol(Liquid):
    def __init__(self, name, density, strenght):
        super().__init__(name, density) # вначале мы вызываем родительский инициализатор, который позволит установить наши первые 2 свойства
        self.strenght = strenght  #(max = 1 = 100%)

    def eduit_strenght(self, val):
        self.strenght = val  # изменение крепости

    def print_info(self):
        print(f'Liquid {self.name!r} (density = {self.density} kg/m^3, strength = {self.strenght:.0%}).')

    def calc_v(self, m):
        v = super().calc_v(m)
        # содержание чистого спирта = v * % спирта
        v_alc = round(v * self.strenght, 2)
        print(f'The volume of alcohol in {m} kg of {self.name} is {v_alc} m^3.')
        return v, v_alc # возвращает кортеж - общий объем и объем спирта


    def calc_m(self, v):
        m = super().calc_m(v)
        # содержание чистого спирта = v * % спирта
        m_alc = round(m * self.strenght, 2)
        print(f'The weight of alcohol in {v} m^3 of {self.name} is {m_alc} kg.')
        return m, m_alc  # возвращает кортеж - общий объем и объем спирта





a = Alcohol('Wine', 1064.2, 0.14) # 14 - добавляем %, если 0,14, то с флагами играемся {self.density:0%}
a.print_info()

a.edit_density(1000)
a.print_info()

print()

a.calc_m(0.5)
a.calc_v(300)

print()

a.print_info()
a.eduit_strenght(0.2)
#print(a.strenght) # к методу напрямую чтобы распечатать, т.к. в самом классе АЛкоголь метода принт нет
a.print_info()