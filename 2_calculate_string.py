#  Создать текстовый файл (не программно), сохранить в нем несколько строк,
#  выполнить подсчет количества строк, количества слов в каждой строке
#  подойдет файл из первого задания

with open("strings.txt", "r", encoding='utf-8') as my_file:
    my_list = my_file.readlines()
print(f'Количество строк в файле {len(my_list)}')
for num, string in enumerate(my_list):
    print(f'В {num + 1} строке количество слов - {len(string.split())}')
