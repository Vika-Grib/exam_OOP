"""Внести изменения в созданные классы следующим образом:
b.	динамические свойства классов “Point” и “Time” должны иметь модификатор доступа protected;
c.	определить методы getter и setter для свойств с модификаторами доступа private и protected;
d.	любое взаимодействие с private и protected свойствами  должно производиться посредством соответствующих методов getter и setter.
	Продемонстрировать работу измененных классов.
"""

class Time:
# статическое свойство: часовой пояс (строка в формате “UTC+/-число(от -12 до 15)”)
    pref = 'UTC'
    time_offset = 2
    time_offset_str = '{pref}{time_offset:+}'.format(pref=pref, time_offset=time_offset)
    # time_offset_str = f'{pref}+{time_offset:+}' т.к. f-строка генерируется один раз в том месте,
    # где она создается, поэтому нужно использовать format, чтобылюбое нужное знаечение потом- также подставлялось
    time_offset_min = -12
    time_offset_max = 14

    def __init__(self, h, m, s):
        if Time.is_correct(h, m, s):
            self.set_h(h)
            self.set_m(m)
            self.set_s(s)
            # self._h = h
            # self._m = m
            # self._s = s
            self.print_info()
        else:
            self.set_h(0)
            self.set_m(0)
            self.set_s(0)
            #self.h = self.m = self.s = 0
        print('Wrong data!')

    def __del__(self):
        print(f'The timestamp {self.get_str()} was deleted!')

    def set_h(self, h):
        self._h = h

    def get_h(self):
        return self._h

    def set_m(self, m):
        self._m = m

    def get_m(self):
        return self._m

    def set_s(self, s):
        self._s = s

    def get_s(self):
        return self._s

# классовые методы: редактировать часовой пояс
    @classmethod
    def edit_time_offset(cls, val):
        if cls.time_offset_min <= val <= cls.time_offset_max:
            cls.time_offset = val
            cls.time_offset_str = '{pref}{time_offset:+}'.format(pref=cls.pref, time_offset=cls.time_offset)
        else:
            print(f'Wrong value: {cls.pref} time offset should be from {cls.time_offset_min} to {cls.time_offset_max} only!')
            print('-' * 50)
# статические методы: проверка корректности заданных величин (часов, минут, секунд),
# перевод заданного значения из формата Час:Минута:Секунда в секунды и наоборот
    @staticmethod
    def is_correct(h, m, s):
        return h in range(0, 24) and m in range(0, 60) and s in range(0, 60)  # возвр логическое значение: если все 3 величины правильные, то будет возращено True

    @staticmethod
    def to_sec(h, m, s):
        return s + m * 60 + h * 3600     # sec = s + m * 60 + h * 3600

    @staticmethod
    def from_sec(sec):
        h = sec // 3600
        sec %= 3600 # сколько секунд осталось
        m = sec // 60
        s = sec % 60 # сколько секунд осталось
        return h, m, s  # будет возварщен кортеж

    # конструктор: вызывает конструктор родительского класса и выводит сообщение о создании нового момента времени
    def __new__(cls, *args, **kwargs):
        print('New timestamp was created.')
        return super().__new__(cls)


    def get_str(self):
        return f'{self.get_h():02}:{self.get_m():02}:{self.get_s():02} {Time.time_offset_str}'


    def print_info(self):
            print(f'The timestamp {self.get_str()}')  # два знака, если 8, то нужно 08 и заполнитель 0


    # методы: вычисление разницы между двумя моментами времени в секундах
    def calc_diff(self, timestamp):
        sec1 = Time.to_sec(self.get_h(), self.get_m(), self.get_s())
        sec2 = Time.to_sec(timestamp.get_h(), timestamp.get_m(), timestamp.get_s())
        res = sec2 - sec1
        print(f'The difference between {timestamp.get_str()} and {self.get_str()} is {res:+} sec.')

    # сложение с заданным количеством секунд
    def plus_sec(self, val):
        print(f'Add {val} sec to {self.get_str()}: ')
        sec = Time.to_sec(self.get_h(), self.get_m(), self.get_s())   # переводим всё в секунды
        sec += val
        # self.h, self.m, self.s = Time.from_sec(sec)  # передаем общее количество сек и переводим из сек в норм время
        h, m, s = Time.from_sec(sec)
        self.set_h(h)
        self.set_m(m)
        self.set_s(s)
        self.print_info()


    def minus_sec(self, val):
        print(f'Subtrack {val} sec from {self.get_str()}: ')
        sec = Time.to_sec(self.get_h(), self.get_m(), self.get_s())
        sec -= val
        # self.h, self.m, self.s = Time.from_sec(sec)
        h, m, s = Time.from_sec(sec)
        self.set_h(h)
        self.set_m(m)
        self.set_s(s)
        self.print_info()

    # сравнение двух моментов времени
    def is_the_same_moment(self, timestamp):  # timestamp - полученный объект
        res = self.get_h() == timestamp.get_h() \
              and self.get_m() == timestamp.get_m() \
              and self.get_s() == timestamp.get_s()
        print(f'The timestamp {self.get_str()} and {timestamp.get_str()} '
              f'are {"not" if not res else ""} the same moments.')
        return res


t1 = Time(25, 18, 0)
t2 = Time(5, 89, 3)
t3 = Time(3, 16, 68)
print()

Time.edit_time_offset(100)
print(Time.time_offset_str)
print()

Time.edit_time_offset(-4)
print(Time.time_offset_str)
print()

t = Time(14, 5, 37)
t.print_info()
print()

t.calc_diff(Time(8, 0, 3))  # сразу пишем объект внутри с которым сравниваем 21 934 sec
t.plus_sec(320)     # + 5m 20s
t.minus_sec(3665)   # - 1h 1m 5s
print()

t.is_the_same_moment(Time(13, 9, 52))
t.is_the_same_moment(Time(13, 9, 53))
print()