#  Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
#  практических и лабораторных занятий по этому предмету и их количество.
#  Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#  Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import googletrans
translator = googletrans.Translator()
courses = {}


def del_rubbish(x):
    new_string = ''
    for letter in x:
        if ord(letter) <= 122 and letter != ':' and letter != '(' and letter != ')':
            new_string = new_string + ''.join([letter])
    return new_string


with open("text_6.txt", "r", encoding='utf-8') as my_file:
    for string in my_file:
        course = del_rubbish(string).split()
        for one in course:
            hours = sum(map(int, (el for el in course[1:] if el.isdigit())))
            courses.update({translator.translate(course[0], dest="ru").text.capitalize(): hours})
print(courses)
