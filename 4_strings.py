# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input("Введите строку разделенную пробелами ")
user_list = user_string.split()
for ind, word in enumerate(user_list):
    word = word[:10]
    print(ind+1, word)
