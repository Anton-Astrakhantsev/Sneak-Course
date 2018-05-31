# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import requests
import time


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


def get_inf_fun(token, met, user):
    params = {
        'access_token': token,
        'user_id': user,
        'v': '5.78'
    }
    fil = requests.get('https://api.vk.com/method/{}.get'.format(met), params)
    return fil.json()['response']['items']


def get_mass_group_fun(token, fr_list):
    gr_list = []
    for fr in fr_list:
        p = {
            'user_id': fr,
            'access_token': token,
            'v': '5.78'
        }
        res = requests.get('https://api.vk.com/method/groups.get', p)
        time.sleep(0.34)
        if str(res.json().keys()) == 'dict_keys([\'error\'])':
            continue
        gr_list.extend(res.json()['response']['items'])
    return list(set(gr_list))


def comp_group_fun(user_list, friend_list):
    res_list = []
    for u in user_list:
        if u not in friend_list:
            res_list.append(u)
    return res_list


def paint_fun(token, gr_list):
    print("\nСекретные группы:")
    for g in gr_list:
        p = {
            'access_token': token,
            'group_id': g,
            'fields': 'name',
            'v': '5.78'
        }
        gro = requests.get('https://api.vk.com/method/groups.getById', p)
        time.sleep(0.34)
        gr_name = str(gro.json()['response'][0]['name'])
        gr_link = 'https://vk.com/id' + str(g)
        print("{} — {}".format(gr_name, gr_link))


def main():
    t = get_token_fun()
    usr = input("Пожалуйста, введите id жертвы: ")
    user_fr = get_inf_fun(t, 'friends', usr)
    print("Программа будет выполняться примерно {} секунд".format(0.34 * len(user_fr)))
    user_gr = get_inf_fun(t, 'groups', usr)
    friend_gr = get_mass_group_fun(t, user_fr)
    alone_list = comp_group_fun(user_gr, friend_gr)
    paint_fun(t, alone_list)


main()
