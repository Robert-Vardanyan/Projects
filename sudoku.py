### Rova
### Smart assistant for the game 'Sudoku'
### Version 1.2
import os
os.system('cls')
# patrasti orinakner 
#taxtak = {(0, 0): '5', (0, 1): '3', (0, 2): ' ', (0, 3): ' ', (0, 4): '7', (0, 5): ' ', (0, 6): ' ', (0, 7): ' ', (0, 8): ' ', (1, 0): '6', (1, 1): ' ', (1, 2): ' ', (1, 3): '1', (1, 4): '9', (1, 5): '5', (1, 6): ' ', (1, 7): ' ', (1, 8): ' ', (2, 0): ' ', (2, 1): '9', (2, 2): '8', (2, 3): ' ', (2, 4): ' ', (2, 5): ' ', (2, 6): ' ', (2, 7): '6', (2, 8): ' ', (3, 0): '8', (3, 1): ' ', (3, 2): ' ', (3, 3): ' ', (3, 4): '6', (3, 5): ' ', (3, 6): ' ', (3, 7): ' ', (3, 8): '3', (4, 0): '4', (4, 1): ' ', (4, 2): ' ', (4, 3): '8', (4, 4): ' ', (4, 5): '3', (4, 6): ' ', (4, 7): ' ', (4, 8): '1', (5, 0): '7', (5, 1): ' ', (5, 2): ' ', (5, 3): ' ', (5, 4): '2', (5, 5): ' ', (5, 6): ' ', (5, 7): ' ', (5, 8): '6', (6, 0): ' ', (6, 1): '6', (6, 2): ' ', (6, 3): ' ', (6, 4): ' ', (6, 5): ' ', (6, 6): '2', (6, 7): '8', (6, 8): ' ', (7, 0): ' ', (7, 1): ' ', (7, 2): ' ', (7, 3): '4', (7, 4): '1', (7, 5): '9', (7, 6): ' ', (7, 7): ' ', (7, 8): '5', (8, 0): ' ', (8, 1): ' ', (8, 2): ' ', (8, 3): ' ', (8, 4): '8', (8, 5): ' ', (8, 6): ' ', (8, 7): '7', (8, 8): '9'}
#taxtak =  {(0, 0): '3', (0, 1): ' ', (0, 2): ' ', (0, 3): '8', (0, 4): ' ', (0, 5): '1', (0, 6): ' ', (0, 7): ' ', (0, 8): '2', (1, 0): '2', (1, 1): ' ', (1, 2): '1', (1, 3): ' ', (1, 4): '3', (1, 5): ' ', (1, 6): '6', (1, 7): ' ', (1, 8): '4', (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', (2, 3): '2', (2, 4): ' ', (2, 5): '4', (2, 6): ' ', (2, 7): ' ', (2, 8): ' ', (3, 0): '8', (3, 1): ' ', (3, 2): '9', (3, 3): ' ', (3, 4): ' ', (3, 5): ' ', (3, 6): '1', (3, 7): ' ', (3, 8): '6', (4, 0): ' ', (4, 1): '6', (4, 2): ' ', (4, 3): ' ', (4, 4): ' ', (4, 5): ' ', (4, 6): ' ', (4, 7): '5', (4, 8): ' ', (5, 0): '7', (5, 1): ' ', (5, 2): '2', (5, 3): ' ', (5, 4): ' ', (5, 5): ' ', (5, 6): '4', (5, 7): ' ', (5, 8): '9', (6, 0): ' ', (6, 1): ' ', (6, 2): ' ', (6, 3): '5', (6, 4): ' ', (6, 5): '9', (6, 6): ' ', (6, 7): ' ', (6, 8): ' ', (7, 0): '9', (7, 1): ' ', (7, 2): '4', (7, 3): ' ', (7, 4): '8', (7, 5): ' ', (7, 6): '7', (7, 7): ' ', (7, 8): '5', (8, 0): '6', (8, 1): ' ', (8, 2): ' ', (8, 3): '1', (8, 4): ' ', (8, 5): '7', (8, 6): ' ', (8, 7): ' ', (8, 8): '3'}

taxtak = {(0, 0): ' ', (0, 1): ' ', (0, 2): ' ', (0, 3): ' ', (0, 4): ' ', (0, 5): ' ', (0, 6): ' ', (0, 7): ' ', (0, 8): ' ', (1, 0): ' ', (1, 1): ' ', (1, 2): ' ', (1, 3): ' ', (1, 4): ' ', (1, 5): ' ', (1, 6): ' ', (1, 7): ' ', (1, 8): ' ', (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', (2, 3): ' ', (2, 4): ' ', (2, 5): ' ', (2, 6): ' ', (2, 7): ' ', (2, 8): ' ', (3, 0): ' ', (3, 1): ' ', (3, 2): ' ', (3, 3): ' ', (3, 4): ' ', (3, 5): ' ', (3, 6): ' ', (3, 7): ' ', (3, 8): ' ', (4, 0): ' ', (4, 1): ' ', (4, 2): ' ', (4, 3): ' ', (4, 4): ' ', (4, 5): ' ', (4, 6): ' ', (4, 7): ' ', (4, 8): ' ', (5, 0): ' ', (5, 1): ' ', (5, 2): ' ', (5, 3): ' ', (5, 4): ' ', (5, 5): ' ', (5, 6): ' ', (5, 7): ' ', (5, 8): ' ', (6, 0): ' ', (6, 1): ' ', (6, 2): ' ', (6, 3): ' ', (6, 4): ' ', (6, 5): ' ', (6, 6): ' ', (6, 7): ' ', (6, 8): ' ', (7, 0): ' ', (7, 1): ' ', (7, 2): ' ', (7, 3): ' ', (7, 4): ' ', (7, 5): ' ', (7, 6): ' ', (7, 7): ' ', (7, 8): ' ', (8, 0): ' ', (8, 1): ' ', (8, 2): ' ', (8, 3): ' ', (8, 4): ' ', (8, 5): ' ', (8, 6): ' ', (8, 7): ' ', (8, 8): ' '}
print('Fill in the initial layout of the Sudoku')
print('If you are finished, then simply press Enter without input.\n')
while True:
    text_y = input('Input Y: ')
    if text_y == '':
        break
    text_x = input('Input X: ')
    if text_x == '':
        break    
    text_n = input('Input Number: ')
    print()
    if text_n == '':
        break
    else:
        y = int(text_y)
        x = int(text_x)
        n = int(text_n)
        if y > 8 or x > 8 or n > 9 or y < 0 or x < 0 or n < 1:
            print('!!! Wrong input !!!\nIn your input something seems off\nY = 0-8\nX = 0-8\nN = 1-9\nTry one more time !\n')
        else:
            taxtak[(y,x)] = n
n_lracum = -1
while True:
    # print('n_lracum = ',n_lracum)
    def map(taxtak,datark):
        for y in range(-1,10):
            for x in range(-1,9):
                if y == -1 and x != 8:
                    print(' _', end = '')
                elif y == 9 and x != 8:
                    print(' ‾', end = '')
                elif x == -1:
                    print('|', end = '')
                elif y != -1 and y != 9 :
                    if taxtak[(y,x)] != ' ':
                        print(taxtak[(y,x)] , end = '|')
                    else:
                        print(' ', end = '|')
                        datark.append((y,x))
            print()
        return ''
    datark = []
    n_lracum += 1
    if n_lracum == 0:
        print('\n'+'🏁'*33)
        print('\nSkzbnakan tesqy' )
    else:
        print('\n'+'🏁'*33)
        print('\nLracum # ',n_lracum )
    print(map(taxtak,datark))
    
    kub_1 = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    kub_2 = [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
    kub_3 = [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]

    kub_4 = [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)]
    kub_5 = [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)]
    kub_6 = [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)]

    kub_7 = [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)]
    kub_8 = [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)]
    kub_9 = [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]

    keys = taxtak.keys()
    keys = list(keys)

    def poisk_variantner(h_arjeqy):
        v_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        v_list_ashx = v_list.copy()
        for v in h_arjeqy:
            if v  in v_list:
                v_list_ashx.remove(v)
        return v_list_ashx
    def poisk_tvyalner():
        if not len(datark):
            exit()
        for p in datark:
            tarberakner = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            keys_ashx = keys.copy()
            hertakan_kety = p
            hertakani_y = []
            h_y_arjeqy = []
            hertakani_x = []
            h_x_arjeqy = []
            hertakani_kubiky = []
            h_k_arjeqy = []
            for q in keys:
                if hertakan_kety in kub_1 and q in kub_1 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                elif hertakan_kety in kub_2 and q in kub_2 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                elif hertakan_kety in kub_3 and q in kub_3 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                elif hertakan_kety in kub_4 and q in kub_4 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                elif hertakan_kety in kub_5 and q in kub_5 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                elif hertakan_kety in kub_6 and q in kub_6 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                elif hertakan_kety in kub_7 and q in kub_7 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                elif hertakan_kety in kub_8 and q in kub_8 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                elif hertakan_kety in kub_9 and q in kub_9 and q in keys_ashx:
                    hertakani_kubiky.append(q)
                    h_k_arjeqy.append(taxtak[q])
                if hertakan_kety[1] == q[1] and q in keys_ashx:
                    hertakani_y.append(q)
                    h_y_arjeqy.append(taxtak[q])
                if hertakan_kety[0] == q[0] and q in keys_ashx:
                    hertakani_x.append(q)
                    h_x_arjeqy.append(taxtak[q])
            v_k = poisk_variantner(h_k_arjeqy)
            v_y = poisk_variantner(h_y_arjeqy)
            v_x = poisk_variantner(h_x_arjeqy)
            t = []
            for v_t in tarberakner:
                if v_t in v_k and v_t in v_y and v_t in v_x:
                    t.append(v_t)
            if len(t) == 1:
                taxtak[hertakan_kety] = t[0]
                print('d_kety',hertakan_kety,'\tt =',t[0])
    print(poisk_tvyalner())