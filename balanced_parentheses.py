### Rova
### Balanced parentheses v. 1.0

import random
n = int(input("Input n = "))

for i in range(n):
    print (f'{i:2}|', end = ' ')
    choice = "()"
    tox = []
    for j in range(1000):
        tox_into = ''
        for k in range(i):
            if k == 0  or  tox_into.count('(') == tox_into.count(')'):
                skobka_1 = '('
                skobka_2 = random.choice(choice)
            elif tox_into.count('(') < tox_into.count(')'):
                skobka_1 = '('
                skobka_2 = random.choice(choice)
            elif tox_into.count('(') > tox_into.count(')'):
                skobka_1 = ')'
                skobka_2 = random.choice(choice)
            tox_into += skobka_1
            tox_into += skobka_2
        if tox_into not in tox  and (tox_into.count('(') == tox_into.count(')')):
            tox.append(tox_into)
        tox_into_2 = '('*i + ')'*i
        if tox_into_2 not in tox:
            tox.append(tox_into_2)
    print(tox)