# Поляков Андрей ИУ7-12Б
# Найти предложения, в которых че-то с с средним арифметическим

TEXT = ["Им овладело чувство полной беспомощности. Прежде всего он не знал,",  # Ввод текста
        "правда ли, что год. Около этого несомненно: он был почти",
        "уверен, что ему лет, а родился он в, но теперь",
        "невозможно установить никакую дату точнее, чем с ошибкой в год или",
        "два. А 1+1 для кого,3+1 вдруг озадачился он,3+3 пишется этот дневник? Для будущего,",
        "для тех, кто еще не родился. Мысль его покружила над сомнительной",
        "датой, запи1+1санной на листе, и вд9+9руг наткнула1+1сь на новоязовское",
        "слово двоемыслие. И впервые стал виден весь масштаб его затеи."]

strs = []
curr_str = []
for i_line in range(len(TEXT)):
    curr = ""
    for char in TEXT[i_line]:
        curr += char
        if char == "." or char == "?" or char == "!":
            curr_str.append(curr)
            strs.append(curr_str)
            curr = ""
            curr_str = []
    curr_str.append(curr)
for i in range(len(strs)):
    buff = ""
    for subline in strs[i]:
        buff += subline + " "
    strs[i] = buff

res_ar = []
for line in strs:
    arr_res = []
    in_v = False
    in_plus = False
    in_minus = False
    res = 0
    buffer = ""
    for char in line:
        if char.isdigit() or (char == "-" and not in_v):
            if char == "-":
                in_minus = True
                continue
            elif not in_v:
                in_v = True
            buffer += char
        elif in_v:
            if char == "+":
                if in_minus:
                    res -= int(buffer)
                    in_minus, in_plus = False, True
                    buffer = ""
                else:
                    res += int(buffer)
                    buffer = ""
                    in_plus = True
            elif char == "-":
                if in_plus:
                    res += int(buffer)
                    in_plus, in_minus = False, True
                    buffer = ""
                else:
                    res += int(buffer)
                    buffer = ""
                    in_minus = True
            else:
                if in_minus:
                    res -= int(buffer)
                else:
                    res += int(buffer)
                arr_res.append(res)
                buffer = ""
                res = 0
                in_v, in_plus, in_minus = False, False, False
        else:
            in_v, in_plus, in_minus = False, False, False
    res_ar.append(arr_res)

reses = [False] * len(res_ar)
for i_line in range(len(res_ar)):
    s = 0
    if res_ar[i_line]:
        for x in res_ar[i_line]:
            s += x
        av = s / len(res_ar[i_line])
        num = 0
        for x in res_ar[i_line]:
            if x <= av:
                num += 1
        if num >= len(res_ar[i_line]) / 2:
            reses[i_line] = True
for i_line in range(len(reses)):
    if reses[i_line]:
        print(strs[i_line])
