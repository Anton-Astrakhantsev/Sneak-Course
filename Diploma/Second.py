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

TOKEN = '113f7204886b24e2f46ca99d464a894cb586c6d30775177a50875e5762065deee24e9a1219aba0dff94e5'


def get_inf_fun(met, user):
    params = {
        'access_token': TOKEN,
        'user_id': user,
        'v': '5.78'
    }
    fil = requests.get('https://api.vk.com/method/{}.get'.format(met), params)
    return fil.json()['response']['items']


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


fr = get_inf_fun('friends', 10844340)


def strange(fr_list):
    i = 0
    t_list = []
    a_list = []
    for f in fr_list:
        t_list.append(f)
        i += 1
        if i == 25:
            a_list.append(t_list)
            t_list = []
            i = 0
        if f == fr_list[len(fr_list)-1]:
            a_list.append(t_list)
    return a_list


llist = strange(fr)

def interaction (fr_list):
    for fr in fr_list:
        p = {
            'code': '''
            var avg = {};
            var lim = avg.length;
            var i = 0;
            var grp = 0;
            while (i<lim) {{ 
            grp = grp + API.groups.get({{"user_id": avg[i]}}).items; 
            }}
            return grp;
            '''.format(fr),
            'access_token': TOKEN,
            'v': '5.78'
        }
        print(p)
        gro = requests.get('https://api.vk.com/method/execute', p)
        print(gro.json())
        time.sleep(0.34)

interaction(llist)
