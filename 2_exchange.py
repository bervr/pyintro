# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()
#second_list = input('введите список')
second_list = [11, 12.74, False, '', "Non", -99, 0, 'Hi', 12]
result_list = []
for el in range(len(second_list)+1):
    if not el%2:
        temp_list = second_list[el:el+2]
        temp_list.reverse()
        result_list.extend(temp_list)
print(result_list)
