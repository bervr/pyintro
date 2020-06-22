# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

import itertools

try:
    start_cooking = int(input('Введите цифрами с чего начать '))
    stop_cooking_the_pot = int(input('Введите цифрами до скольки считать '))

    for el in itertools.count(start_cooking):
        if el > stop_cooking_the_pot:
            break
        else:
            print(el)
except:
    print('Нас устроят только цифры')


с = 0
for el in itertools.cycle("Привет!"):
    if с > stop_cooking_the_pot:
        break
    print(el)
    с += 1