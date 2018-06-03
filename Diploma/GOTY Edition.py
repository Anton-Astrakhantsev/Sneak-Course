# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import requests
import time
import json


def get_token_fun():
    app_id = 6486003
    auth_url = 'https://oauth.vk.com/authorize'
    auth_data = {
        'client_id': app_id,
        'display': 'page',
        'scope': 'friends, groups',
        'response_type': 'token',
        'v': '5.78'
    }
    print("Пожалуйста, перейдите по ссылке и скопируйте token:")
    print('?'.join((auth_url, urlencode(auth_data))))
    token = input("\nПожалуйста, вставьте token: ")
    return token


def get_inf_fun(token, meth, user):
    params = {
        'access_token': token,
        'user_id': user,
        'v': '5.78'
    }
    fil = requests.get('https://api.vk.com/method/{}.get'.format(meth), params)
    return fil.json()['response']['items']


class VKSacrifice:

    def __init__(self, token, name):
        self.token = token
        self.s_name = name

    def id(self):
        try:
            return int(self.s_name)
        except:
            param = {
                'access_token': self.token,
                'screen_name': self.s_name,
                'v': '5.78'
            }
            res = requests.get('https://api.vk.com/method/utils.resolveScreenName', param)
            return res.json()['response']['object_id']

    def friends(self):
        return get_inf_fun(self.token, 'friends', self.id())

    def groups(self):
        return get_inf_fun(self.token, 'groups', self.id())


def check_fun(number, or_list):
    if number == len(or_list):
        print("Программа завершена на 99%")
    else:
        step = lambda num: num / len(or_list) * 10 // 1
        if step(number) != step(number - 1):
            print("Программа завершена на {}%".format(int(step(number) * 10)))


def get_mass_group_fun(token, fr_list):
    gr_list = []
    num = 0
    for fr in fr_list:
        param = {
            'user_id': fr,
            'access_token': token,
            'v': '5.78'
        }
        res = requests.get('https://api.vk.com/method/groups.get', param)

        num += 1
        check_fun(num, fr_list)

        if str(res.json().keys()) == 'dict_keys([\'error\'])':
            continue
        else:
            gr_list.extend(res.json()['response']['items'])

        time.sleep(0.34)
    return list(set(gr_list))


def comp_group_fun(user_list, friend_list):
    res_list = []
    for user in user_list:
        if user not in friend_list:
            res_list.append(user)
    return res_list


def conv_gr_dict_fun(token, gr_list):
    gr_dict_list = []
    for gr in gr_list:
        gr_dict = {}
        param = {
            'access_token': token,
            'group_id': gr,
            'fields': 'name,id,members_count',
            'v': '5.78'
        }
        res = requests.get('https://api.vk.com/method/groups.getById', param)
        gr_dict['name'] = str(res.json()['response'][0]['name'])
        gr_dict['id'] = str(res.json()['response'][0]['id'])
        gr_dict['members_count'] = str(res.json()['response'][0]['members_count'])
        gr_dict_list.append(gr_dict)
        time.sleep(0.34)
    return gr_dict_list


def create_json_fun(token, gr_dict, iden):
    param = {
        'access_token': token,
        'user_ids': iden,
        'fields': 'first_name',
        'name_case': 'gen',
        'v': '5.78'
    }
    res = requests.get('https://api.vk.com/method/users.get', param)
    name = res.json()['response'][0]['first_name']
    with open('Секретные группы {}.json'.format(name), 'w', encoding='utf-8') as f:
        json.dump(gr_dict, f, indent=2)


def main():
    token = get_token_fun()
    name = input("Пожалуйста, введите идентификатор жертвы: ")
    victim = VKSacrifice(token, name)
    print("Программа будет выполняться примерно {} секунд".format(0.34 * len(victim.friends())))
    friend_gr = get_mass_group_fun(token, victim.friends())
    alone_list = comp_group_fun(victim.groups(), friend_gr)
    alone_dict = conv_gr_dict_fun(token, alone_list)
    create_json_fun(token, alone_dict, victim.id())
    print("Программа завершена на 100%")


main()
