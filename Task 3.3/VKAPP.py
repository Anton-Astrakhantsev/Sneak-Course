# Программа готова на 60%
# Это пробный вариант. Он возвращает список общих друзей между двумя пользователями.
# Но Я собирался дополнить эту программу дополнительным функционалом

person_f = input()
person_s = input()

params={
    'access_token': TOKEN,
    'v': '5.73',
    'source_uid': person_f,
    'target_uid': person_s
}

resp = requests.get('https://api.vk.com/method/friends.getMutual', params)
r = resp.json()
print(r['response'])
