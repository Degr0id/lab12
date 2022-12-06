# Поляков Андрей ИУ7-12Б

import tasks


def output(txt):  # Вывод текста
    print("")
    for line in txt:
        print(line)
    print("")


def check_if_word(word):
    if word.isalpha():
        return True
    elif word.count("-") == 1 and 0 < word.find("-") < len(word) - 1 and word.replace("-", "").isalpha():
        return True
    return False


def max_len_calc(txt):  # Самая длинная строка
    max_l = 0
    for line in txt:
        max_l = max(max_l, len(line))
    return max_l


def menu(txt):
    while True:
        print("\nМеню")
        print("1) Выровнять текст по левому краю.\n"
              "2) Выровнять текст по правому краю.\n"
              "3) Выровнять текст по ширине.\n"
              "4) Удаление всех вхождений заданного слова.\n"
              "5) Замена одного слова другим во всём тексте.\n"
              "6) Умножение и деление над целыми числами внутри текста.\n"
              "7) Найти предложение, в котором кол-во слов, содержащих каждую букву 2 и более раз, максимально.\n"
              "8) Вывести текст на экран.\n"
              "9) Очистить ввод\n"
              "0) Выход.")
        user_input = input("Ввод-->")
        if user_input == "1":
            tasks.task1(txt)
            output(txt)
        elif user_input == "2":
            tasks.task2(txt)
            output(txt)
        elif user_input == "3":
            tasks.task3(txt)
            output(txt)
        elif user_input == "4":
            tasks.task4(txt)
            #output(txt)
        elif user_input == "5":
            tasks.task5(txt)
            #output(txt)
        elif user_input == "6":
            tasks.task6(txt)
            output(txt)
        elif user_input == "7":
            res = tasks.task7(txt)
            if res == 0:
                print("")
                output(txt)
        elif user_input == "8":
            output(txt)
        elif user_input == "9":
            clear = "\n" * 100
            print(clear)
        elif user_input == "0":
            break
        else:
            print("Некорректный ввод, пожалуйста введите номер операции\n")
