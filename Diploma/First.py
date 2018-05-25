from urllib.parse import urlencode
import requests
import time

APP_ID = 6486003
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends,groups',
    'response_type': 'token',
    'v': '5.78'
}
# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '21410103c646988900018522c4c9fad9718b4d3cf5b266c4baba21742b55e3b82328ff4afb42a22d0e417'


def get_inf_fun(met):
    params = {
        'access_token': TOKEN,
        'v': '5.78'
    }
    fil = requests.get('https://api.vk.com/method/{}.get'.format(met), params)
    return fil.json()['response']['items']


def interaction(gr_list, fr_list):
    alone_group_list = []
    for group in gr_list:
        c = 0
        for friend in fr_list:
            p = {
                'access_token': TOKEN,
                'v': '5.78',
                'group_id': group,
                'user_id': friend
            }
            mem = requests.get('https://api.vk.com/method/groups.isMember', p)
            c += int(mem.json()['response'])
            time.sleep(0.34)
        if c == 0:
            alone_group_list.append(group)
    return alone_group_list


def painter(gr_list):
    print("Секретные группы:")
    for g in gr_list:
        p = {
            'access_token': TOKEN,
            'group_id': g,
            'fields': 'name',
            'v': '5.78'
        }
        gro = requests.get('https://api.vk.com/method/groups.getById', p)
        time.sleep(0.34)
        gr_name = str(gro.json()['response'][0]['name'])
        gr_link = 'https://vk.com/id' + str(g)
        print("{} — {}".format(gr_name, gr_link))


fr = get_inf_fun('friends')
gr = get_inf_fun('groups')
intr = interaction(gr[0:10], fr[0:10])
painter(intr)
