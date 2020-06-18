# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text

def int_func(text):
    """
    Возвращает слово с загравной буквы если исходное слово сотояло из маленьких латинских букв. Если нет то ругается
    :param text: hello
    :return: Hello
    :param text: hеllo
    :return: 'Wrong symbols has in your word'
    :param text: аавып
    :return: 'Wrong symbols has in your word'
    :param text: adsd0dsf
    :return: 'Wrong symbols has in your word'
    """

    my_list=['']
    for i in text:
        if 97 <= ord(i) <= 122:
            my_list.append(i)
        else:
            # print('Ну что такое? Предупреждал же, что проверю')
            my_list=['']
            break
    z = (''.join(my_list)).capitalize() if my_list != [''] else 'Wrong symbols has in your word'
    return z

user_word = input('введите слово, только из маленьких латинских букв, я проверю! ')
print(int_func(user_word))

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
temp_list = []
user_string = input('введите строку, только из маленьких латинских букв и пробелов, я проверю! ').split()
for i in user_string:
   if int_func(i) == 'Wrong symbols has in your word':
       temp_list.clear()
       print('в строке есть подозрительные символы')
       break
   else:
       temp_list.append(int_func(i))
print(' '.join(temp_list))
print('На этом всё')


