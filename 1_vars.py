# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.


var_test1 = 12.07
var_test2 = 'строка'
var_buffer = None
print(f'Допустим пока переменные равны var_test1 = {var_test1} (тип {type(var_test1)}) и var_test2 = {var_test2} ')
var_test1 = (input('Введите число '))
if var_test1.isdigit():
    var_test1 = float(var_test1)
var_test2 = input('Введите произвольную строку ')
print(f'Теперь переменные равны var_test1 = {var_test1} (тип {type(var_test1)}) и var_test2 = {var_test2} ')
