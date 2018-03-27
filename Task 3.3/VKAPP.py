from urllib.parse import urlencode
import requests

APP_ID = 6422981
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends,status',
    'response_type': 'token',
    'v': '5.73'
}

# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '178a9b32c608d3587ef3c7d3232f68b26b5c540381f77f7a2a3b7f94bf1387c7aab6c3ccc62510fa3a607'


def step_first(): # Функция для ввода ID
    id_f = input("Введите ваш ID: ")
    id_s = input("Введите ID другого пользователя: ")
    return [id_f, id_s]


def step_second(x, y, t): # Функция для создания параметров
    if x == '':
        par = {
            'access_token': t,
            'v': '5.73',
            'target_uid': y
        }
    else:
        par = {
            'access_token': t,
            'v': '5.73',
            'source_uid': x,
            'target_uid': y
        }
    return par


def step_third(p): # Функция для создания списка
    resp = requests.get('https://api.vk.com/method/friends.getMutual', p)
    return resp.json()['response']


def step_fourth(l): # Функция для вывода списка друзей
    print("Общие друзья:")
    for friend in l:
        para = {
            'user_ids': friend,
            'fields': 'first_name,last_name',
            'v': '5.73'
        }
        fr = requests.get('https://api.vk.com/method/users.get', para).json()
        name = " ".join((fr['response'][0]['first_name'], fr['response'][0]['last_name']))
        link = 'https://vk.com/id' + str(friend)
        print("{} — {}".format(name, link))


def main():
    step_f = step_first()
    params = step_second(step_f[0], step_f[1], TOKEN)
    friends_list = step_third(params)
    step_fourth(friends_list)


main()
