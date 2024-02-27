### Rova
### Pascal's triangle v. 1.0

t_n = int(input("Input n = "))
tox_0 = []
tox_1 = []
tox_2 = []
summ = 0

for i in range(t_n):
    
    if i == 0 or i % 3 == 0:
        n = 1 
        for j in range(i+1):
            if j == 0 or j == i:
                tox_0.append(1)
            elif j == 1 or j == i -1 :
                tox_0.append(i)
            else:
                summ = tox_2[n] + tox_2[n+1]
                n += 1
                tox_0.append(summ)
        print(" "*(t_n-1-i) , tox_0)
        tox_1.clear()
    elif i == 1 or (i-1) % 3 == 0:
        n = 1 
        for j in range(i+1):
            if j == 0 or j == i:
                tox_1.append(1)
            elif j == 1 or j == i -1 :
                tox_1.append(i)
            else:
                summ = tox_0[n] + tox_0[n+1]
                n += 1
                tox_1.append(summ)
        print(" "*(t_n-1-i) ,tox_1)
        tox_2.clear()
    elif i == 2 or (i-2) % 3 == 0 :
        n = 1
        for j in range(i+1):
            if j == 0 or j == i:
                tox_2.append(1)
            elif j == 1 or j == i -1 :
                tox_2.append(i)
            else:
                summ = tox_1[n] + tox_1[n+1]
                n += 1
                tox_2.append(summ)
        print(" "*(t_n-1-i) ,tox_2)
        tox_0.clear()