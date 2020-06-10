# Узнайте у пользователя число n.Найдите сумму чисел
# n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

user_num = str(abs(int(float(input('Введите целое положительное число '))))) #убираем дробь, минус, возвращаем в строку

result_num =int(user_num) + int(user_num +user_num) +int(user_num + user_num + user_num)

print(f'Чудо-число будет {result_num}')

