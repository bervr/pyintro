# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open("text_3.txt", "r", encoding='utf-8') as my_file:
   my_list= my_file.readlines()
employees ={}
print('Заплата меньше $20k у сотрудников: ')
for  string in my_list:
    employee = string.split()
    if float(employee[1]) <20000:
        print(employee[0])
    employees.update({employee[0]:float(employee[1])})
print(f'Средняя зарплата на сотрудника {sum(employees.values())/len(employees.keys())}')

