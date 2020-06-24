# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_text_block = ''
import googletrans
translator = googletrans.Translator()
with open("text_4.txt", "r", encoding='utf-8') as my_file:
    for string in my_file:
        number = string.split()
        my_text_block += "".join([f'{(translator.translate(number[0],dest="ru").text).capitalize()} - {number[2]}\n'])
with open("new_4.txt", "a", encoding='utf-8') as new_file:
    new_file.write(my_text_block)
#pip install googletrans

