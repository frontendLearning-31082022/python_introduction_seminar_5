# 2) Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
import re

if __name__ == '__main__':
    count_lines = 0
    file = open('task_2_file.txt')
    for line in file:
        # words = [s for s in line.split(" ") if len(s) >0]
        words_len = len(re.findall(r'\w+', line))

        print(f"Words at {count_lines} line IS {words_len}")
        count_lines += 1
    print(f"File has {count_lines} lines ")
