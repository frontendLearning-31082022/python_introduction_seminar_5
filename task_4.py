# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import re

if __name__ == '__main__':
    file = open('task_4_file.txt', mode="r", encoding="utf-8")
    file_output = open('task_4_file_output.txt', mode="a", encoding="utf-8")

    dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три',
                  'Four': 'Четырке'}

    for line in file:
        all_words = re.findall(r'\w+', line)
        nessary_word = [i for i in all_words if dictionary.__contains__(i)]

        file_output.write(re.sub(
            nessary_word[0], dictionary[nessary_word[0]], line))
