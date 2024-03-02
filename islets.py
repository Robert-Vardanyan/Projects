### Rova
### Program: Find islands count on map.
### Version: 1.5
import random
import os
os.system('cls') 
map_x,map_y = 10,10
choice = '0001'
cordinatner = []
for i in range(map_y):
    for j in range(map_x):
        k = random.choice(choice)
        if k == '1':
            cord_k = [i,j]
            cordinatner.append(cord_k)
def poisk(cordinatner, h =0):
    cordinatner_ashx = cordinatner.copy()
    if not kxzi:
        a = cordinatner[0]
        kxzi.append(a)
        cordinatner.remove(a)
        return poisk(cordinatner)
    elif h > len(kxzi) -1:
        return kxzi
    else:
        for l in cordinatner_ashx:
            if kxzi[h][0] - 1 == l[0] and (kxzi[h][1] -1 == l[1] or kxzi[h][1] == l[1] or kxzi[h][1]  == l[1]-1):
                kxzi.append(l)
                cordinatner.remove(l)
            if kxzi[h][0] == l[0] and (kxzi[h][1] -1 == l[1] or kxzi[h][1]  == l[1]-1):
                kxzi.append(l)
                cordinatner.remove(l)
            if kxzi[h][0] == l[0] -1 and (kxzi[h][1] -1 == l[1] or kxzi[h][1] == l[1] or kxzi[h][1]  == l[1]-1):
                kxzi.append(l)
                cordinatner.remove(l)
        return poisk(cordinatner, h + 1)
n = 0
kxziner = []
while True:
    kxzi = []
    n += 1
    print(f'kxzi {n}',poisk(cordinatner))
    kxziner += kxzi
    if len(cordinatner) == 0:
        print('qanaky',n)
        break
for y in range(map_y):
    for x in range(map_x):
        kety = [y,x]
        if kety in kxziner:
            print('🟨', end = '')
        else:
            print('🌊', end = '')
    print()