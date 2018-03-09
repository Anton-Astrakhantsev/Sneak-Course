def cut_string(st):  # эта программа пробразует код формата "Яйцо | 2 | шт" в нужный для cook_book словарь
    sp = st.split(' | ')
    dict_sp = {'ingridient_name': sp[0].lower(), 'quantity': int(sp[1]), 'measure': sp[2]}
    return dict_sp


def open_book(link):
    cook_book = {}
    with open(link, encoding='utf-8') as f:
        for line in f:
            x = line.strip().lower()
            in_list = []
            time = int(f.readline().strip())
            while time != 0:
                in_list.append(cut_string(f.readline().strip()))
                time -= 1
            cook_book[x] = in_list
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    cook_book = open_book('Ингредиенты.txt')
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


create_shop_list()
