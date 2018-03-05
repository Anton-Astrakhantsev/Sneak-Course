import chardet

origin = []


def text(u):
    with open(u, 'rb') as f:
        data = f.read()
        code = chardet.detect(data)
        print("Кодировка: {} с вероятностью {}\n".format(code['encoding'], code['confidence']))
    with open(u, encoding=code['encoding']) as f:
        for line in f:
            origin.append(line.lower().strip().split(' '))


te = input("Введите название файла ")
text(te)

fix = lambda l: sum(l, [])
origin = fix(origin)

seven = []


for i in origin:
    if len(i) > 6:
        seven.append(i)


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


for i in range(10):
    f1 = i + 1
    f2 = final[i]
    f3 = half_final.count(final[i])
    f4 = razz(half_final.count(final[i]))
    print("{} место - \"{}\", упоминается {} {}".format(f1, f2, f3, f4))
