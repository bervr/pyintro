# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
my_string = 'start'
while my_string != '':
    with open("strings.txt", "a", encoding='utf-8') as my_file:
        my_string = input('Напишите что вы думаете ')
        print(my_string, file=my_file)
