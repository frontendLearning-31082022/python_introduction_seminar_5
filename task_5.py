# 5) Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

if __name__ == '__main__':
    digits_ram = [random.uniform(-15000.01, 69111) for i in range(1, 40)]
    one_write_ssd_safe = ' '.join(str(x) for x in digits_ram)

    file = open('task_5_file_output.txt', mode="r+", encoding="utf-8")
    file.write(one_write_ssd_safe)

    one_string_short_file = file.read()
    sum = sum([float(i) for i in one_string_short_file.split(" ")])

    print("Sum digits - " + "{:.2f}".format(sum))
