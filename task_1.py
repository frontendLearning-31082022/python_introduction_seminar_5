# 1) Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

if __name__ == '__main__':

    while True:
        print("Input somethint text. To quiet - empty line")
        inputed = input()
        if len(inputed) == 0:
            exit(0)
        with open("task_1.txt", 'a') as file1:
            file1.write(inputed + "\n")


