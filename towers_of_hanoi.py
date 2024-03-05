### Rova
### Smart assistant for the game 'Towers of Hanoi'
### Version 1.0
def move(n):
    s = 0
    qaylq = ['1','2','3']
    n_qayly = 0
    if n % 2 == 0:
        while True:
            if len(syun_3) == n:
                print(f'Finish\nn = {n}\nsteps((2 ** {n}) -1) = {n_qayly}')
                break
            else:
                if qaylq[s] == '1':
                    s += 1
                    n_qayly += 1
                    if not syun_2:
                        syun_2.append(syun_1.pop(-1))
                        print( f'{n_qayly:3} | {syun_2[-1]} 1-->2\n')
                    elif not syun_1:
                        syun_1.append(syun_2.pop(-1))
                        print( f'{n_qayly:3} | {syun_1[-1]} 2-->1\n')
                    elif tarer.index(syun_1[-1]) < tarer.index(syun_2[-1]):
                        syun_2.append(syun_1.pop(-1))
                        print( f'{n_qayly:3} | {syun_2[-1]} 1-->2\n')
                    elif tarer.index(syun_1[-1]) > tarer.index(syun_2[-1]):
                        syun_1.append(syun_2.pop(-1))
                        print( f'{n_qayly:3} | {syun_1[-1]} 2-->1\n')
                elif qaylq[s] == '2':
                    s += 1
                    n_qayly += 1
                    if not syun_3:
                        syun_3.append(syun_1.pop(-1))
                        print( f'{n_qayly:3} | {syun_3[-1]} 1-->3\n')
                    elif tarer.index(syun_1[-1]) < tarer.index(syun_3[-1]):
                        syun_3.append(syun_1.pop(-1))
                        print( f'{n_qayly:3} | {syun_3[-1]} 1-->3\n')
                    elif tarer.index(syun_1[-1]) > tarer.index(syun_3[-1]):
                        syun_1.append(syun_3.pop(-1))
                        print( f'{n_qayly:3} | {syun_1[-1]} 3-->1\n')
                elif qaylq[s] == '3':
                    s = 0
                    n_qayly += 1
                    if tarer.index(syun_2[-1]) < tarer.index(syun_3[-1]):
                        syun_3.append(syun_2.pop(-1))
                        print( f'{n_qayly:3} | {syun_3[-1]} 2-->3\n')
                    elif tarer.index(syun_2[-1]) > tarer.index(syun_3[-1]):
                        syun_2.append(syun_3.pop(-1))
                        print( f'{n_qayly:3} | {syun_2[-1]} 3-->2\n')          
    elif n % 2 != 0:
        while True:
            if len(syun_3) == n:
                print(f'Finish\nn = {n}\nsteps((2 ** {n}) -1) = {n_qayly}')
                break
            else:
                if qaylq[s] == '1':
                    s += 1
                    n_qayly += 1
                    if not syun_3:
                        syun_3.append(syun_1.pop(-1))
                        print( f'{n_qayly:3} | {syun_3[-1]} 1-->3\n')
                    elif tarer.index(syun_1[-1]) < tarer.index(syun_3[-1]):
                        syun_3.append(syun_1.pop(-1))
                        print( f'{n_qayly:3} | {syun_3[-1]} 1-->3\n')
                    elif tarer.index(syun_1[-1]) > tarer.index(syun_3[-1]):
                        syun_1.append(syun_3.pop(-1))
                        print( f'{n_qayly:3} | {syun_1[-1]} 3-->1\n')
                elif qaylq[s] == '2':
                    s += 1
                    n_qayly += 1
                    if not syun_2:
                        syun_2.append(syun_1.pop(-1))
                        print( f'{n_qayly:3} | {syun_2[-1]} 1-->2\n')
                    elif not syun_1:
                        syun_1.append(syun_2.pop(-1))
                        print( f'{n_qayly:3} | {syun_1[-1]} 2-->1\n')
                    elif tarer.index(syun_1[-1]) < tarer.index(syun_2[-1]):
                        syun_2.append(syun_1.pop(-1))
                        print( f'{n_qayly:3} | {syun_2[-1]} 1-->2\n')
                    elif tarer.index(syun_1[-1]) > tarer.index(syun_2[-1]):
                        syun_1.append(syun_2.pop(-1))
                        print( f'{n_qayly:3} | {syun_1[-1]} 2-->1\n')
                elif qaylq[s] == '3':
                    s = 0
                    n_qayly += 1
                    if tarer.index(syun_2[-1]) < tarer.index(syun_3[-1]):
                        syun_3.append(syun_2.pop(-1))
                        print( f'{n_qayly:3} | {syun_3[-1]} 2-->3\n')
                    elif tarer.index(syun_2[-1]) > tarer.index(syun_3[-1]):
                        syun_2.append(syun_3.pop(-1))
                        print( f'{n_qayly:3} | {syun_2[-1]} 3-->2\n')
        
n = int(input('Input n: '))
if n < 1 or n > 52:
    print('Wrong input!\nmin(n) = 1\nmax(n) = 52')
    exit()
syun_1 = []
syun_2 = []
syun_3 = []
tarer = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(n):
    syun_1.append(tarer[i])
syun_1 = syun_1[::-1]
print(move(n))