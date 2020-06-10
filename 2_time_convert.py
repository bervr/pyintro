# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.


def append_zero(time_part):
    if time_part >= 10: # если больше либо равно 10 нули добавлять не надо
        time_part
    elif time_part>0:
        time_part= '0'+ str(time_part)  # если больше 0 но меньше 10 добавляем один ноль впереди
    else:
        time_part = '00'
    return time_part

time_raw = int(float(input('Введите время в секундах числом, желательно целым (и положительным) ')))
# дропаем дробную часть, преобразуем в число
if time_raw < 0:
    time_raw = -1 * time_raw  # если всеже отрицательное
hours = append_zero(time_raw // 3600)
minutes = append_zero((time_raw % 3600)//60)
seconds = append_zero(time_raw % 60)
print (f'время {hours}:{minutes}:{seconds}')

