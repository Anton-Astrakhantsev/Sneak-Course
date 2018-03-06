import json

origin = []


def nor(p):
    return p.lower().strip().split()


def text(u):
    with open(u, encoding='utf-8') as f:
        inf = json.load(f)
        inf = inf['rss']['channel']
        origin.append(nor(inf["description"]))
        for i in inf['items']:
            origin.append(nor(i["description"]))
            origin.append(nor(i["title"]))


te = input("Введите название файла ")
text(te)

fix = lambda l: sum(l, [])
origin = fix(origin)

seven = list(filter(lambda s: len(s) > 6, origin))

half_final = sorted(seven, key=seven.count)
half_final.reverse()

final = [half_final[0]]

p = 1
while len(final) < 10:
    if half_final[p] != final[len(final) - 1]:
        final.append(half_final[p])
    p += 1


def razz(o):
    o = str(o)
    if (o[len(o) - 1] == '2') or (o[len(o) - 1] == '3') or (o[len(o) - 1] == '4'):
        return "раза"
    else:
        return "раз"


print('')
for i in range(10):
    f1 = i + 1
    f2 = final[i]
    f3 = half_final.count(final[i])
    f4 = razz(half_final.count(final[i]))
    print("{} место - \"{}\", упоминается {} {}".format(f1, f2, f3, f4))
