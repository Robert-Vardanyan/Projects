### Rova
### Smart assistant for the game 'Towers of Hanoi'
### Version 1.5
print("\n👋😄 Hello, I'm the Smart Assistant created by #Rova to help you figure out the steps needed\n\t\tto win as quickly as possible in the game 'Towers of Hanoi'.\n")
def arajin_erkrord(syun_1,syun_2,n_qayly):
    if not syun_2:
        syun_2.append(syun_1.pop(-1))
        return f'{n_qayly:3}) {syun_2[-1]} |1 --> 2|'
    elif not syun_1:
        syun_1.append(syun_2.pop(-1))
        return f'{n_qayly:3}) {syun_1[-1]} |2 --> 1|'
    elif tarer.index(syun_1[-1]) < tarer.index(syun_2[-1]):
        syun_2.append(syun_1.pop(-1))
        return f'{n_qayly:3}) {syun_2[-1]} |1 --> 2|'
    elif tarer.index(syun_1[-1]) > tarer.index(syun_2[-1]):
        syun_1.append(syun_2.pop(-1))
        return f'{n_qayly:3}) {syun_1[-1]} |2 --> 1|'
def arajin_errord(syun_1,syun_3,n_qayly):
    if not syun_3:
        syun_3.append(syun_1.pop(-1))
        return f'{n_qayly:3}) {syun_3[-1]} |1 --> 3|'
    elif tarer.index(syun_1[-1]) < tarer.index(syun_3[-1]):
        syun_3.append(syun_1.pop(-1))
        return f'{n_qayly:3}) {syun_3[-1]} |1 --> 3|'
    elif tarer.index(syun_1[-1]) > tarer.index(syun_3[-1]):
        syun_1.append(syun_3.pop(-1))
        return f'{n_qayly:3}) {syun_1[-1]} |3 --> 1|'
def erkrord_errord(syun_2,syun_3,n_qayly):
    if tarer.index(syun_2[-1]) < tarer.index(syun_3[-1]):
        syun_3.append(syun_2.pop(-1))
        return f'{n_qayly:3}) {syun_3[-1]} |2 --> 3|'
    elif tarer.index(syun_2[-1]) > tarer.index(syun_3[-1]):
        syun_2.append(syun_3.pop(-1))
        return f'{n_qayly:3}) {syun_2[-1]} |3 --> 2|' 
def move(n):
    s = 0
    qaylq = ['1','2','3']
    n_qayly = 0
    if n % 2 == 0:
        while True:
            if len(syun_3) == n:
                return f'\n🏁🏁🏁 Finish 🏁🏁🏁\n\n⭕️ Rings: {n}\n🥏 Total count of steps:  {n_qayly}\n🤓 Formula for calculating the number of steps:\t( (2^{n}) - 1 )'
            else:
                if qaylq[s] == '1':
                    s += 1
                    n_qayly += 1
                    print(arajin_erkrord(syun_1,syun_2,n_qayly))
                elif qaylq[s] == '2':
                    s += 1
                    n_qayly += 1
                    print(arajin_errord(syun_1,syun_3,n_qayly))
                elif qaylq[s] == '3':
                    s = 0
                    n_qayly += 1
                    print(erkrord_errord(syun_2,syun_3,n_qayly))
    elif n % 2 != 0:
        while True:
            if len(syun_3) == n:
                return f'\n🏁🏁🏁 Finish 🏁🏁🏁\n\n⭕️ Rings: {n}\n🥏 Total count of steps:  {n_qayly}\n🤓 Formula for calculating the number of steps:\t( (2^{n}) - 1 )'
            else:
                if qaylq[s] == '1':
                    s += 1
                    n_qayly += 1
                    print(arajin_errord(syun_1,syun_3,n_qayly))
                elif qaylq[s] == '2':
                    s += 1
                    n_qayly += 1
                    print(arajin_erkrord(syun_1,syun_2,n_qayly))
                elif qaylq[s] == '3':
                    s = 0
                    n_qayly += 1
                    print(erkrord_errord(syun_2,syun_3,n_qayly))    
n = int(input('Count of rings: '))
if n < 1 or n > 52:
    print('\n   ❌ Wrong input ❌\n❌ Minimum count = 1 ❌\n❌ Maximum count = 52❌')
    exit()
print('Move the rings according to the numbered steps:\n')
syun_1,syun_2,syun_3 = [],[],[]
tarer = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(n):
    syun_1.append(tarer[i])
syun_1 = syun_1[::-1]
print(move(n))