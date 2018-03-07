import chardet


def getting_information(u):
    origin = []
    with open(u, 'rb') as f:
        data = f.read()
        code = chardet.detect(data)
        print("Кодировка: {} с вероятностью {}\n".format(code['encoding'], code['confidence']))
    with open(u, encoding=code['encoding']) as f:
        for line in f:
            origin.append(line.lower().strip().split())
    return origin


def p_bloomed(start_list):
    fix = lambda l: sum(l, [])
    res_list = fix(start_list)
    return res_list


def p_cut(start_list):
    res_list = list(filter(lambda s: len(s) > 6, start_list))
    return res_list


def p_pointed(start_list):
    res_list = sorted(start_list, key=start_list.count)
    res_list.reverse()
    return res_list


def preparing_information(origin_list):
    step_one = p_bloomed(origin_list)
    step_two = p_cut(step_one)
    step_three = p_pointed(step_two)
    return step_three


def analyzing_information(origin_list):
    final_list = [origin_list[0]]
    p = 1
    while len(final_list) < 10:
        if origin_list[p] not in final_list:
            final_list.append(origin_list[p])
        p += 1
    return final_list


def corr_answer(num):
    num = str(num)
    if (num[len(num) - 1] == "2") or (num[len(num) - 1] == '3') or (num[len(num) - 1] == '4'):
        return "раза"
    else:
        return "раз"


def showing_result(analyzed_list, origin_list):
    for i in range(10):
        f1 = i + 1
        f2 = analyzed_list[i]
        f3 = origin_list.count(analyzed_list[i])
        f4 = corr_answer(origin_list.count(analyzed_list[i]))
        print("{} место - \"{}\", упоминается {} {}".format(f1, f2, f3, f4))


def start():
    origin = input("Введите название файла ")
    first = getting_infarmation(origin)
    second = preparing_information(first)
    three = analyzing_information(second)
    final = showing_result(three, second)


start()
