# 3) Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Пример файла:
# Иванов 23543.12
# Петров 13749.32
import random
import re

if __name__ == '__main__':
    juniors = []
    salaries = []

    file = open('task_3_file.txt', mode="r", encoding="utf-8")
    for line in file:
        salary = float(re.search(r'\d+(\.\d+){0,}', line).group(0))
        surname = re.search(r'\w+', line).group(0)

        if float(salary) < 20000:
            juniors.append(surname)
        salaries.append(salary)

    print(f"Less than 20000 list - {juniors} \n"
          f"averange for salaries - " +
          "{:.2f}".format(sum(salaries) / len(salaries)))

    # for i in range(1,40):
    #     print("{:.2f}".format(random.uniform(15000.01, 69111)))
