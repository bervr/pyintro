# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, string):
        self.string = string

    @classmethod
    def get_numeric(cls, num):
        try:
            num_2 = list(map(int, num.split('-')))
        except:
            print("Не верный формат ввода!")
            return 0
        else:
            cls.validate(num_2)


    @staticmethod
    def validate(num_1):
        if num_1[0] in range(1,32) and num_1[1] in range(1,13) and num_1[2] in range(0,2100):
            print(f'{"-".join(map(str,num_1))}  is a valid date')
        else:
            print(f'{"-".join(map(str,num_1))} - invalid date!')


date = Date(1)
date.get_numeric('31-12-2020')
date.get_numeric('23-июля-2020')
date.get_numeric('23-99-2020')
date.get_numeric('01-01-2099')


