# Поляков Андрей ИУ7-12Б

import tools as t


def task1(txt):  # Выровнять текст по левому краю.
    for i in range(len(txt)):
        txt[i] = txt[i].strip()
        while "  " in txt[i]:
            txt[i] = txt[i].replace("  ", " ")


def task2(txt):  # Выровнять текст по правому краю.
    task1(txt)
    max_l = t.max_len_calc(txt)
    for i in range(len(txt)):
        txt[i] = f"{' ' * (max_l - len(txt[i]))}{txt[i]}"


def task3(txt):  # Выровнять текст по центру.
    task1(txt)
    max_l = t.max_len_calc(txt)
    for i in range(len(txt)):
        l_line = len(txt[i])
        if l_line == 0:
            continue
        n_gap, max_rep = divmod(max_l - l_line + txt[i].count(" "), txt[i].count(" "))
        txt[i] = txt[i].replace(" ", " " * n_gap).replace(" " * n_gap, " " * (n_gap + 1), max_rep)


def task4(txt):  # Удаление всех вхождений заданного слова.
    while True:
        word = input("Cлово: ").strip()  # Ввод слова с проверкой
        if t.check_if_word(word):
            break
        print("Пожалуйста введите слово")
    for i_line in range(len(txt)):
        sf_pos = 0
        capitalized = False
        while True:
            if capitalized:
                word = word.lower()
                capitalized = False
            i_wd = txt[i_line][sf_pos:].find(word)
            maybe_cap = txt[i_line][sf_pos:].find(word.capitalize())
            if maybe_cap != -1 and (maybe_cap < i_wd or i_wd == -1):
                word = word.capitalize()
                i_wd = maybe_cap
                capitalized = True
            if i_wd == -1:
                break
            else:
                i_wd += sf_pos
            if i_wd >= len(txt[i_line]):
                break
            if word == "м" or word == "й" and txt[i_line][i_wd - 2].isdigit():
                pass
            elif not ((i_wd + len(word) < len(txt[i_line]) and txt[i_line][i_wd + len(word)].isalpha())
                      or (i_wd > 0 and txt[i_line][i_wd - 1].isalpha())):
                cnt = 1
                while txt[i_line][i_wd - cnt] == " ":  # Удаление слова с пробелами перед ним
                    word = " " + word
                    cnt += 1
                txt[i_line] = txt[i_line][:sf_pos] + txt[i_line][sf_pos:].replace(word, "", 1)
                word = word.strip()
            sf_pos = i_wd + 1


def task5(txt):  # Замена одного слова другим во всём тексте.
    while True:
        old_word = input("Старое слово: ").strip()  # Ввод слов с проверкой
        new_word = input("Новое слово: ").strip()
        if old_word == new_word:
            print("Слова не могут совпадать")
        elif t.check_if_word(old_word) and t.check_if_word(new_word):
            break
        print("Пожалуйста введите слова")
    for i_line in range(len(txt)):
        sf_pos = 0
        capitalized = False
        while True:
            if capitalized:
                old_word = old_word.lower()
                new_word = new_word.lower()
                capitalized = False
            i_wd = txt[i_line][sf_pos:].find(old_word)
            maybe_cap = txt[i_line][sf_pos:].find(old_word.capitalize())
            if maybe_cap != -1 and (maybe_cap < i_wd or i_wd == -1):
                i_wd = maybe_cap
                old_word = old_word.capitalize()
                new_word = new_word.capitalize()
                capitalized = True
            if i_wd == -1:
                break
            else:
                i_wd += sf_pos
            if i_wd >= len(txt[i_line]):
                break
            if not ((i_wd + len(old_word) < len(txt[i_line]) and txt[i_line][i_wd + len(old_word)].isalpha())
                    or (i_wd > 0 and txt[i_line][i_wd - 1].isalpha())):
                txt[i_line] = txt[i_line][:sf_pos] + txt[i_line][sf_pos:].replace(old_word, new_word, 1)
            sf_pos = i_wd + 1


def task6(txt):  # Умножение и деление над целыми числами внутри текста
    for i_line in range(len(txt)):  # Вычисление выражений в каждой строке
        while " /" in txt[i_line] or "/ " in txt[i_line] or " *" in txt[i_line] or "* " in txt[i_line]:
            txt[i_line] = txt[i_line].replace(" /", "/")  # Исключение "х1_/_х2" --> "x1/x2"
            txt[i_line] = txt[i_line].replace(" *", "*")
            txt[i_line] = txt[i_line].replace("/ ", "/")
            txt[i_line] = txt[i_line].replace("* ", "*")
        arr_res = []
        in_v = False
        in_mult = False  # Три состояния
        in_div = False
        res = 0
        buffer = ""
        st = None
        for i_char in range(len(txt[i_line])):
            if txt[i_line][i_char].isdigit():  # Если число
                if not in_v:
                    in_v = True
                    st = i_char
                buffer += txt[i_line][i_char]
            elif in_v:
                if txt[i_line][i_char] == "*":  # Переход в умножение
                    if in_div:
                        res = res / int(buffer) if buffer != "0" and res is not None else None
                        in_div, in_mult = False, True
                        buffer = ""
                    elif in_mult:
                        res = res * int(buffer) if res is not None else None
                        buffer = ""
                    else:
                        res += int(buffer)
                        buffer = ""
                        in_mult = True
                elif txt[i_line][i_char] == "/":  # Переход в деление
                    if in_div:
                        if buffer == "":
                            continue
                        res = res / int(buffer) if buffer != "0" and res is not None else None
                        buffer = ""
                    elif in_mult:
                        res = res * int(buffer) if res is not None else None
                        in_div, in_mult = True, False
                        buffer = ""
                    else:
                        res += int(buffer)
                        buffer = ""
                        in_div = True
                else:  # выход из текущего выражения
                    if in_div:
                        res = res / int(buffer) if buffer != "0" and res is not None else None
                    elif in_mult:
                        res = res * int(buffer) if res is not None else None
                    else:
                        res += int(buffer)
                    arr_res.append((res, st, i_char))
                    buffer = ""
                    st = None
                    res = 0
                    in_v, in_div, in_mult = False, False, False
        if buffer != "":
            if in_div:
                res = res / int(buffer) if buffer != "0" and res is not None else None
            elif in_mult:
                res = res * int(buffer) if res is not None else None
            else:
                res += int(buffer)
            arr_res.append((res, st, len(txt[i_line]) - 1))
        delt = 0
        for res, st, ed in arr_res:
            temp = txt[i_line][st - delt:ed - delt]  # Замена
            if res is None:
                res = temp
            elif temp.endswith(" "):
                res = f"{res:.5g} "
            else:
                res = f"{res:.5g}"
            txt[i_line] = txt[i_line].replace(temp, res)
            delt += len(temp) - len(res)


def task7(txt):  # Найти предложение, в котором кол-во слов, содержащих каждую букву 2 и более раз, максимально.
    strs = []
    curr_str = []
    if len(txt) == 0:
        print("Текст пуст")
        return -1
    for i_line in range(len(txt)):
        curr = ""
        for char in txt[i_line]:
            curr += char
            if char == "." or char == "?" or char == "!":
                curr_str.append([curr, i_line])
                strs.append(curr_str)
                curr = ""
                curr_str = []
        curr_str.append([curr, i_line])  # Двумерный массив предложений и их разбиения по строкам
    max_cnt = 0
    i_str_max = 0
    for i_string in range(len(strs)):  # Подстчет нужных слов
        curr = []
        for j in strs[i_string]:
            curr += j[0].split()
        cnt = 0
        for word in curr:
            for char in word:
                if not char.isalpha():
                    word = word.replace(char, "")
            if word == "":
                continue
            for char in word:
                word = word.replace(char, "", 1)
                if char in word:
                    word = word.replace(char, "")
                    if word == "":
                        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            i_str_max = i_string
    print("Строка:")
    res_str = []
    for part in strs[i_str_max]:
        while "  " in part[0]:
            part[0] = part[0].replace("  ", " ")  # Вывод сттроки
        res_str.append(part[0])
    for part in res_str:
        for s in part:
            print(s, end='')
        print(" ", end='')
    delt = 0
    for del_part in strs[i_str_max]:  # Удаление предложения
        txt[del_part[1] - delt] = txt[del_part[1] - delt].replace(del_part[0], "")
        txt[del_part[1] - delt] = txt[del_part[1] - delt].strip()
        if txt[del_part[1] - delt] == "":
            del (txt[del_part[1] - delt])
            delt += 1
    return 0
