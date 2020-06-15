# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month_number = abs(int(float(input('Введите значение месяца числом от 1 до 12 '))))
month_number if 0 < month_number <= 12 else print('от 1 до 12!')
year_dict = {12: "Зима", 1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
             9: "Осень", 10: "Осень", 11: "Осень"}
year_list = [[12, 1, 2, "Зима"], [3, 4, 5, "Весна"], [6, 7, 8, "Лето"], [9, 10, 11, "Осень"]]
time_of_year = year_dict.get(month_number)
print(time_of_year)
for season in year_list:
    if season.count(month_number):
        time_of_year = season[3]
print(f'Ах, {time_of_year}!')
