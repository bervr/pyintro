#  * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#  Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
#  номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
#  Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
#  например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
continue_key = 'y'
result_list = []
goods_counter = 0
while continue_key == 'y':
    continue_key = (input('Добавить новый товар? y/n '))
    if continue_key == 'n':
        break
    else:
        goods_dict = {}
        goods_counter += 1
        goods_name = input('Введите название товара ')
        goods_price = input('Введите цену товара ')
        goods_quantity = input('Введите количество товара ')
        goods_units = input('Введите единицы измерения товара ')
        confirm = input(f'Все верно? Добавить новый товар номер {goods_counter}, {goods_name}, цена {goods_price}, '
                        f'количество {goods_quantity} {goods_units}? y/n ')
        if confirm == 'y':
            goods_tuple = (goods_counter,{})
            goods_tuple[1].update({'name': goods_name, 'price': goods_price, 'quantity': goods_quantity,
                                   'units': goods_units})
            #  не знаю как ключи русскими сделать, и времени не осталось...  #  пофиксить когда нибудь
            result_list.append(goods_tuple)
            # print(goods_tuple)
            # print(goods_dict)
            #print(result_list)
        else:
            goods_counter -= 1
            continue
analyst_dict={}
name_list=[]
price_list=[]
quantity_list=[]
unit_list=[]
if result_list:
    for unit in range(len(result_list)):
        name_list.append(result_list[unit][1].get('name'))
        price_list.append(result_list[unit][1].get('price'))
        quantity_list.append(result_list[unit][1].get('quantity'))
        unit_list.append(result_list[unit][1].get('units'))
    analyst_dict.update({'name': name_list, 'price': price_list,'quantity': quantity_list, 'units': unit_list})
    print(analyst_dict)
