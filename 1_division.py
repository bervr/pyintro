# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_2(digit_1, digit_2):
    """ возвращает результат деления первого числа на второе с точностью до 2х знаков после запятой

    :param digit_1:
    :param digit_2:
    :return:
    """
    try:
        quotient = digit_1 / digit_2
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    except TypeError:
        return 'Не умею делить строки, вводите числа цифрами'
    else:
        return round(quotient, 2)


def input_float(number):
    try:
        user_digit = float(input(f'Введите число номер {number} '))
    except ValueError:
        return "введите число цифрами"
    else:
        return user_digit


dividend = input_float(1)
print(dividend)
divisor = input_float(2)
print(division_2(dividend, divisor))
