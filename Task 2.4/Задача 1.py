import os
# готово на 40%

# 1. собирает список первоначальных документов
# 2. ищет среди них слово
# 3. изменяет список файлов
# 4. повторить 2

def all_files():
    time_list = os.listdir(path=".")
    for i in time_list:
        if i[-3:] = 'sql':
            res_list.append(i)


def peek(link): # поиск в файле
    with open(link, encoding='utf-8') as f:
        num = 0
        data = f.read()
        for line in inf:
            num += line.count(word)
        if num != 0: res_list.append(link)


def find_and_point():
    res_list = []
    while 1:
        word = input('Введите строку: ')
        for i in res_list:
            
