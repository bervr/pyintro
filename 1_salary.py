#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(hours, price):
    try:
        worker_salary = float(hours) * float(price)
        return worker_salary
    except:
        print('введите выработку и ставку цифрами')


# hours =argv[1]
# price = argv[2]
script_name, hours, price = argv
print(salary(hours, price))
