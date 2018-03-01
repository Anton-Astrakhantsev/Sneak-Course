# В принципе т.к. у нас есть полностью работающий код для словаря cook_book,
# но ингредиенты записаны в другом файле, всю задачу можно свести
# к созданию полностью аналогичного словаря и преминить старыйй код к нему


def cool(st):  # эта программа пробразует код формата "Яйцо | 2 | шт" в нужный для cook_book словарь
    sp = st.split(' | ')
    dict_sp = {'ingridient_name': sp[0].lower(), 'quantity': int(sp[1]), 'measure': sp[2]}
    return dict_sp


cook_book = {}

with open('Ингредиенты.txt', encoding='utf-8') as f:
    for line in f:
        x = str(line).strip().lower()
        in_list = []
        time = int(str(f.readline().strip()))
        while time != 0:
            in_list.append(cool(f.readline().strip()))
            time -= 1
        cook_book[x] = in_list
        f.readline()


# print(cook_book) # в качестве проверки можно убедиться, что новый cook_book сделан полностью по формату старой версии

def get_shop_list_by_dishes(dishes, person_count):
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
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
