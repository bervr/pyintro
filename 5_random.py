# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# # Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

my_text_block = ' '.join(map(str, [random.randint(-1000, 1000) for el in range(15)])) + ' '
with open("new_5.txt", "a+", encoding='utf-8') as new_file:
    new_file.writelines(my_text_block)
    new_file.seek(0)
    full_numbers = new_file.read().split()
print(f'сумма чисел в файле {sum(map(int, full_numbers))}')
