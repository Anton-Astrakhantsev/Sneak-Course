import os


def checker(file_list_one):
    file_list_two = []
    for f in file_list_one:
        if f.endswith('.sql'):
            file_list_two.append(f)
    return file_list_two


def researcher(word, way, file_list):
    next_list = []
    for fi in file_list:
        with open(os.path.join(way, fi), 'rb') as f:
            data = f.readlines()
            for line in data:
                if word in line.decode():
                    next_list.append(fi)
    return list(set(next_list))


def main():
    way = os.path.join(os.path.dirname(__file__), 'Migrations')
    file_list = os.listdir(way)
    file_list = checker(file_list)
    while 1:
        word = input("Введите строку: ")
        next_list = researcher(word, way, file_list)
        print(', '.join(next_list))
        print('Всего:', len(next_list))
        file_list = next_list


main()
