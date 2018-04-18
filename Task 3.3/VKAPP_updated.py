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

TOKEN = '4f27579aba72e3c6eb2a5c8e196225f0c186bd33c0d88a6932b7565d75c89f5d70c19717b3f9bbf397102'
# Эта часть кода служит для получения token

def one_get_parameters(*ids): # Эта функция создает список из параметров для каждого пользователя
    par_list = []
    for id in ids:
        par = {
            'access_token': TOKEN,
            'v': '5.73',
            'target_uid': id
        }
        par_list.append(par)
    return par_list


def second_get_files(par_list): # Эта функция получает общих друзей для каждого id из списка (дубликаты удаляются)
    fr_id_list = []
    for p in par_list:
        resp = requests.get('https://api.vk.com/method/friends.getMutual', p)
        fr_id_list.append(resp.json()['response'])
    fr_id_list_new = list(set(sum(fr_id_list, [])))
    return fr_id_list_new


def third_formalization(fr_id_list): # Эта функция выводит список общих друзей в приятном виде
    print("Общие друзья:")
    for friend in fr_id_list:
        para = {
            'user_ids': friend,
            'fields': 'first_name,last_name',
            'v': '5.73'
        }
        fr = requests.get('https://api.vk.com/method/users.get', para).json()
        name = " ".join((fr['response'][0]['first_name'], fr['response'][0]['last_name']))
        link = 'https://vk.com/id' + str(friend)
        print("{} — {}".format(name, link))


def main(*ids):
    pars = one_get_parameters(*ids)
    fils = second_get_files(pars)
    third_formalization(fils)


main(817836, 7640927)
