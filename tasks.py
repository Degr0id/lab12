# Поляков Андрей ИУ7-12Б

import tools as t


def task1(txt):
    for i in range(len(txt)):
        txt[i] = txt[i].strip()
        while "  " in txt[i]:
            txt[i] = txt[i].replace("  ", " ")


def task2(txt):
    task1(txt)
    max_l = t.max_len_calc(txt)
    for i in range(len(txt)):
        txt[i] = f"{' ' * (max_l - len(txt[i]))}{txt[i]}"


def task3(txt):
    task1(txt)
    max_l = t.max_len_calc(txt)
    for i in range(len(txt)):
        l_line = len(txt[i])
        n_gap, max_rep = divmod(max_l - l_line + txt[i].count(" "), txt[i].count(" "))
        txt[i] = txt[i].replace(" ", " " * n_gap).replace(" " * n_gap, " " * (n_gap + 1), max_rep)


def task4(txt):
    while True:
        word = input("Cлово: ")
        if word.isalpha():
            break
        else:
            print("Пожалуйста введите слово")
    for i_line in range(len(txt)):
        while True:
            i_wd = txt[i_line].find(word)
            if i_wd == -1:
                break
            cnt = 1
            while txt[i_line][i_wd - cnt] == " ":
                word = " " + word
                cnt += 1
            txt[i_line] = txt[i_line].replace(word, "", 1)


def task5(txt):
    while True:
        old_word = input("Старое слово: ")
        new_word = input("Новое слово: ")
        if new_word.isalpha() and old_word.isalpha():
            break
        else:
            print("Пожалуйста введите слово")
    for i_line in range(len(txt)):
        txt[i_line] = txt[i_line].replace(old_word, new_word)


def task6(txt):
    for i_line in range(len(txt)):
        arr_res = []
        in_v = False
        in_mult = False
        in_div = False
        res = 0
        buffer = ""
        st = None
        for i_char in range(len(txt[i_line])):
            if txt[i_line][i_char].isdigit():
                if not in_v:
                    in_v = True
                    st = i_char
                buffer += txt[i_line][i_char]
            elif in_v:
                if txt[i_line][i_char] == " ":
                    continue
                elif txt[i_line][i_char] == "*":
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
                elif txt[i_line][i_char] == "/":
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
                else:
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
        delt = 0
        for res, st, ed in arr_res:
            temp = txt[i_line][st - delt:ed - delt]
            if res is None:
                res = temp
            elif temp.endswith(" "):
                res = f"{res:.5g} "
            else:
                res = f"{res:.5g}"
            txt[i_line] = txt[i_line].replace(temp, res)
            delt += len(temp) - len(res)


def task7(txt):
    strs = []
    curr_str = []
    for i_line in range(len(txt)):
        curr = ""
        for char in txt[i_line]:
            curr += char
            if char == "." or char == "?" or char == "!":
                curr_str.append((curr, i_line))
                strs.append(curr_str)
                curr = ""
                curr_str = []
        curr_str.append((curr, i_line))
    max_cnt = 0
    i_str_max = 0
    for i_string in range(len(strs)):
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
        res_str.append(part[0])
    for part in res_str:
        for s in part:
            print(s, end='')
        print(" ", end='')
    delt = 0
    for del_part in strs[i_str_max]:
        txt[del_part[1] - delt] = txt[del_part[1] - delt].replace(del_part[0], "")
        txt[del_part[1] - delt] = txt[del_part[1] - delt].strip()
        if txt[del_part[1] - delt] == "":
            del (txt[del_part[1] - delt])
            delt += 1
