# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_numbers = input('Введите через пробед что на что поделить ')

try:
    my_list = list(map(int, my_numbers.split()))
    if my_list[1] == 0:
        raise OwnError('Вы делите на ноль')
except ValueError:
    print("Вы ввели не число")
except OwnError as my_error:
    print(my_error)
else:
    print(f'{my_list[0] / my_list[1]} - результат деления')
