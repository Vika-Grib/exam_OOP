""""Внести изменения в созданные классы следующим образом:
a.	динамические свойства класса “Account” должны иметь модификатор доступа private;
c.	определить методы getter и setter для свойств с модификаторами доступа private и protected;
d.	любое взаимодействие с private и protected свойствами должно производиться посредством
соответствующих методов getter и setter.
Продемонстрировать работу измененных классов.
"""

class Account():
    # статические, кот принадлежат самому классу, а не экз класса
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    #конструктор: вызывает конструктор родительского класса и выводит сообщение о создании нового банковского счета;
    def __new__(cls, *args, **kwargs):
        print('New account was created successfully.')  # сначала печатаем и потом вызовем конструктор род класса и вернуть значение
        return super().__new__(cls)

    def __init__(self, num, surname, percent, value = 0): # по умолчанию value = 0, когда откроет счет - то добавим
        # self.__num = num
        # self.__surname = surname
        # self.__percent = percent  # вещественное число max = 1, т.е. меньше 1
        # self.__value = value
        self.set_num(num)
        self.set_surname(surname)
        self.set_percent(percent)
        self.set_value(value)
        print(f'The acount #{self.get_num()} owned by {self.get_surname()} was opened.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'The account #{self.get_num()} owned by {self.get_surname()} was closed.')

    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

    def set_surname(self, surname):
        self.__surname = surname

    def get_surname(self):
        return self.__surname

    def set_percent(self, percent):
        self.__percent = percent

    def get_percent(self):
        return self.__percent

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    #статические методы: перевод суммы в доллары и евро
    @staticmethod
    def convert(value, rate): #value - кот нужно перевести и курс, по которому будем переводить
        return value * rate

    # смена владельца счета
    def edit_owner(self, surname):
        #self.surname = surname
        self.set_surname(surname) # устанавливаем новую фамилию

    # выводит текузую сумму на счету
    def print_balace(self):
        print(f'The current balance is {self.get_value()} {Account.suffix}')

    # снятие заданной суммы
    def withdraw_money(self, val):
        if val > self.get_value(): # берем значение и сравниваем его, а не устанавливаем, поэтому get
            print(f'Unfortunatly, you have not {val} {Account.suffix}')
        else:
            self.set_value(self.get_value() - val)    #self.value -= val
            print(f'{val} {Account.suffix} was successfully withdrawed.')

        self.print_balace()  # обращаемся к нашему методу и распечатываем баланс

    # начисление заданной суммы
    def add_money(self, val):
        self.set_value(self.get_value() + val)  # self.value += val
        print(f'{val} {Account.suffix} was successfully added!')
        self.print_balace()

    # начисление процентов
    def add_percents(self):
        # self.value += self.value * self.percent
        #cur_val = self.get_value() # создаем переменную, чтобы в скобках 2 раза не вызывать метод
        # self.set_value(self.get_value() + self.get_value() * self.get_percent())
        #self.set_value(cur_val + cur_val * self.get_percent()), выносим за скобку и получаем
        self.set_value(self.get_value() * (1 + self.get_percent()))
        print(f'The percent {self.get_percent()} was successfully added.')
        self.print_balace()

    # перевод в доллары и евро
    # (в отличие от аналогичных статических методов, данные методы не принимают параметров)
    def convert_to_usd(self):
        usd_val = Account.convert(self.get_value(), Account.rate_usd)
        print(f'The current balance is {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.get_value(), Account.rate_eur)
        print(f'The current balance is {eur_val} {Account.suffix_eur}.')

    # вывод информации о счете
    def print_info(self):
        print('Acount info: ')
        print('-' * 20)
        print(f'#{self.get_num()}')
        print(f'Owner {self.get_surname()}')
        self.print_balace()
        print(f'Percent: {self.get_percent():%}')
        print('-' * 20)


acc = Account(num = '12345', surname='Ivanov Ivan', percent = 0.03, value=1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_eur_rate(2)
Account.set_usd_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()

acc.edit_owner(surname='Ivanova')
acc.print_info()
print()

acc.add_percents()
print()
acc.set_percent(0.05)
acc.add_percents()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()