import os


def all_files(n_list):
    os.chdir(os.path.join(os.path.dirname(__file__), 'Materials'))
    time_list = os.listdir(path=".")
    for i in time_list:
        if i[-3:] == 'sql':
            n_list.append(i)
    return n_list


def peek(link, word):
    with open(link, encoding='utf-8') as f:
        data = f.readlines()
        num = 0
        for line in data:
            num += line.count(word)
    return num


def show(v_list, v_number):
    print(v_list)
    print("Всего: {}".format(v_number))


def find_and_point():
    f_list = []
    f_list = all_files(f_list)
    print(f_list[0])
    while 1:
        val = 0
        s_list = []
        word = input('Введите строку: ')
        for i in f_list:
            if peek(i, word) != 0:
                s_list.append(i)
                val += peek(i, word)
        show(s_list, val)
        print(len(s_list))
        f_list = s_list


find_and_point()
