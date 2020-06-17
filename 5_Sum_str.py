# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу


def check_input(y):
    """
    проверяет  строку y на число  и символ # и возвращает число до # в виде числовой строки типа str ,
    или поднимает глобальный флаг остановить ввод если получен символ #
    :param y: -12.03
    :return: -12.03
    :param y: 12#36
    :return: 12
    :param y: 779
    :return: 779
    """
    my_list = ['']
    global input_next
    for i in y:
        if ord(i) == 35:
            input_next = False
            break
        elif 45 <= ord(i) <= 57 and ord(i) != 47:
            my_list.append(i)
    z = ''.join(my_list) if my_list != [''] else 0
    return z


def summarize(x):
    """
    Рекурсивно суммирует числа их списка x
    :param x:[12, -5, 1.02]
    :return: 8.02
    """
    if len(x) == 0:
        return 0
    elif len(x) == 1:
        return float(check_input(x[0]))
    else:
        return float(check_input(x[0])) + summarize(x[1:])


print('Вводите числа через пробел, чтобы завершить - введите # ')
user_sum = 0
input_next = True
while input_next:
    user_string = input().split()
    user_sum += summarize(user_string)
    print(user_sum)
print('программа завершена')
