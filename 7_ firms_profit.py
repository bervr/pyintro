# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json

sum_profit = 0
count_profit = 0
result_dict = {}
with open('text_7.txt', 'r', encoding='utf-8') as my_file:
    for string in my_file:
        string = string.split()
        profit = int(string[2]) - int(string[3])
        if profit > 0:
            sum_profit += profit
            count_profit += 1
        result_dict.update({string[0]: profit})
average_profit = sum_profit / count_profit if count_profit > 0 else 'Все в минусе'
result_list = [result_dict, {"average_profit": average_profit}]
#  print(result_list)
with open('text_7.json', 'w', encoding='utf-8') as new_file:
    json.dump(result_list, new_file, indent=2, ensure_ascii=False)
