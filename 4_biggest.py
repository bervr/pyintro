# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = abs(int(float(input('Введите целое положительное число не (больше 16 знаков) '))))
# потому что все врут, а конструкция есть из прошлой задачи
max_digit = 0
while user_num:
    try_digit = user_num % 10
    user_num = user_num // 10
    if try_digit == 9:
        max_digit = 9
        break
    elif try_digit > max_digit:
        max_digit = try_digit
        continue
print(f'Самая большая цифра в введенном числе - {max_digit}')
