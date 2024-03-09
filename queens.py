### Rova
### A smart assistant to place 8 queens on 1 chessboard
### Version 1.0
import random
taxtak = [('a', 1),('a', 2),('a', 3),('a', 4),('a', 5),('a', 6),('a', 7),('a', 8),('b', 1),('b', 2),('b', 3),('b', 4),('b', 5),('b', 6),('b', 7),('b', 8),('c', 1),('c', 2),('c', 3),('c', 4),('c', 5),('c', 6),('c', 7),('c', 8),('d', 1),('d', 2),('d', 3),('d', 4),('d', 5),('d', 6),('d', 7),('d', 8),('e', 1),('e', 2),('e', 3),('e', 4),('e', 5),('e', 6),('e', 7),('e', 8),('f', 1),('f', 2),('f', 3),('f', 4),('f', 5),('f', 6),('f', 7),('f', 8),('g', 1),('g', 2),('g', 3),('g', 4),('g', 5),('g', 6),('g', 7),('g', 8),('h', 1),('h', 2),('h', 3),('h', 4),('h', 5),('h', 6),('h', 7),('h', 8)]
taxtak_ashx = taxtak.copy()
def stugum():
    inp_1 = input("Du menak asa vortex kuzes lini 1 taguhin (ex.a1) = ").lower().strip()
    if len(inp_1) > 2 or inp_1[0] not in 'abcdefgh':
        return 'Chisht kordinatner gri!'
    else:
        return inp_1[0],int(inp_1[1])
def cord_hanum(t_h,taxtak,taxtak_ashx):
    text = 'abcdefgh'
    n_aj = 1
    n_dzax = 1
    for i in taxtak:
        if t_h[0] in i or t_h[1] in i:
            taxtak_ashx.remove(i)
    while True:
        if (text.index(t_h[0])-n_dzax) > -1:
            tar_dzax = text[text.index(t_h[0])-n_dzax]
            if t_h[1] + n_dzax < 9:
                tiv_verev_dzax = t_h[1] + n_dzax
                cord_hertakan_plus_dzax = tar_dzax,tiv_verev_dzax
                if cord_hertakan_plus_dzax in taxtak_ashx:
                    taxtak_ashx.remove(cord_hertakan_plus_dzax)   
            if t_h[1] - n_dzax > 0:
                tiv_nerqev_dzax = t_h[1] - n_dzax
                cord_hertakan_minus_dzax = tar_dzax,tiv_nerqev_dzax
                if cord_hertakan_minus_dzax in taxtak_ashx:
                    taxtak_ashx.remove(cord_hertakan_minus_dzax)
            n_dzax += 1
        elif (text.index(t_h[0])+n_aj) < 8:
            if (text.index(t_h[0])+n_aj) < 8:
                tar_aj = text[text.index(t_h[0])+n_aj]
                if t_h[1] + n_aj < 9:
                    tiv_verev_aj = t_h[1] + n_aj
                    cord_hertakan_plus_aj = tar_aj,tiv_verev_aj
                    if cord_hertakan_plus_aj in taxtak_ashx:
                        taxtak_ashx.remove(cord_hertakan_plus_aj)
                if t_h[1] - n_aj > 0:
                    tiv_nerqev_aj = t_h[1] - n_aj
                    cord_hertakan_minus_aj = tar_aj,tiv_nerqev_aj
                    if cord_hertakan_minus_aj in taxtak_ashx:
                        taxtak_ashx.remove(cord_hertakan_minus_aj)
                n_aj += 1
        else:break 
    return taxtak_ashx 
print("Ari gtnenq inchpes texavorel 8 taguhi mek taxtaki vra")
while True:
    # Taguhi 1
    t_1 = stugum()
    if isinstance(t_1 , tuple):
        break
    else:
        print(t_1)
def lucum(taxtak,taxtak_ashx):
    taxtak_original = taxtak.copy()
    t_2 = random.choice(taxtak)
    taxtak = cord_hanum(t_2,taxtak,taxtak_ashx).copy()
    t_3 = random.choice(taxtak)
    taxtak = cord_hanum(t_3,taxtak,taxtak_ashx).copy()
    t_4 = random.choice(taxtak)
    taxtak = cord_hanum(t_4,taxtak,taxtak_ashx).copy()
    if len(taxtak) == 0:
        taxtak = taxtak_original.copy()
        taxtak_ashx = taxtak.copy()
        return lucum(taxtak,taxtak_ashx)
    t_5 = random.choice(taxtak)
    taxtak = cord_hanum(t_5,taxtak,taxtak_ashx).copy()
    if len(taxtak) == 0:
        taxtak = taxtak_original.copy()
        taxtak_ashx = taxtak.copy()
        return lucum(taxtak,taxtak_ashx)
    t_6 = random.choice(taxtak)
    taxtak = cord_hanum(t_6,taxtak,taxtak_ashx).copy()
    if len(taxtak) == 0:
        taxtak = taxtak_original.copy()
        taxtak_ashx = taxtak.copy()
        return lucum(taxtak,taxtak_ashx)
    t_7 = random.choice(taxtak)
    taxtak = cord_hanum(t_7,taxtak,taxtak_ashx).copy()
    if len(taxtak) == 0:
        taxtak = taxtak_original.copy()
        taxtak_ashx = taxtak.copy()
        return lucum(taxtak,taxtak_ashx)
    t_8 = random.choice(taxtak)
    taxtak = cord_hanum(t_8,taxtak,taxtak_ashx).copy()
    return t_1,t_2,t_3,t_4,t_5,t_6,t_7,t_8
taxtak_1 = cord_hanum(t_1,taxtak,taxtak_ashx).copy()
lucumner = lucum(taxtak_1,taxtak_ashx)
for i in range(8,-1,-1):
    for j in ' abcdefgh':
        if j == ' ':
            print(i, end = '|')
        elif i == t_1[1] and j == t_1[0]:
            print('💢', end = '')
        elif i == lucumner[1][1] and j == lucumner[1][0]:
            print('💢', end = '')  
        elif i == lucumner[2][1] and j == lucumner[2][0]:
            print('💢', end = '')
        elif i == lucumner[3][1] and j == lucumner[3][0]:
            print('💢', end = '')
        elif i == lucumner[4][1] and j == lucumner[4][0]:
            print('💢', end = '')
        elif i == lucumner[5][1] and j == lucumner[5][0]:
            print('💢', end = '')
        elif i == lucumner[6][1] and j == lucumner[6][0]:
            print('💢', end = '')
        elif i == lucumner[7][1] and j == lucumner[7][0]:
            print('💢', end = '')                 
        elif i == 0 and j != ' ':
            print(f' {j}', end = '')
        elif (j in "aceg" and i % 2 != 0) or (j in "bdfh" and i % 2 == 0):
            print("⬛️", end = '')
        else:
            print("⬜️", end = '')
    print()
lucumner = list(lucumner)
lucumner.sort()
print('Lucumnern en:',lucumner)