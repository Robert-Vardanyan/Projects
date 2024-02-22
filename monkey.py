# #Rova
# #Monkey Game update !
# #New game with smart snake!
# #Monkey game v.2.0 
# #   EXIT ---> 0
# #   *map(with every point -1) 
# #   *banana generation
# #   *life = 3  
# #   *if you touch a cactus - 1 life
# #   *if snake touch Monkey -1 life
# #   *control without press enter button 

import random
import msvcrt
import os
#tvyalner
kyanq = 3   
point = 0
point_0 = 0

#qartez
map_x = 30 #int(input("Input MAP(X) = ")) 
map_y = 30 #int(input("Input MAP(Y) = "))

# kapiki haytnvely
x_monkey = random.randint(0,map_x)
y_monkey = random.randint(0,map_y)

# oci haytnvely
x_oc = map_x // 2
y_oc = map_y // 2

# #banani 1 haytnvelu vayry
x_banan_0 = random.randint(0,map_x-1)
y_banan_0 = random.randint(0,map_y-1)
if x_banan_0 == x_monkey:
    x_banan_0 = random.randint(0,map_x-1)
if y_banan_0 == y_monkey:
    y_banan_0 = random.randint(0,map_y-1)

#qani qayl kani kapiky (glxavor while)
while True:
    os.system('cls') 
    #oci sharjvely
    #inadu em senc arel te che vor shat xelaci oc er linum shat hard er linum ))
    def oci_qaylq(x_oc,y_oc):
        choice = 'xy'
        qayli_yntrutyun = random.choice(choice)
        if qayli_yntrutyun == 'x':
            if x_monkey >= x_oc and x_oc != map_x :
                x_oc += 1
                return x_oc,y_oc
            elif x_monkey < x_oc and x_oc != 0:
                x_oc -= 1
                return x_oc,y_oc
            else:
                return x_oc,y_oc
        elif qayli_yntrutyun == 'y':
            if y_monkey >= y_oc and y_oc != map_y:
                y_oc += 1
                return x_oc,y_oc
            elif y_monkey < y_oc and y_oc != 0:
                y_oc -= 1
                return x_oc,y_oc
            else:
                return x_oc,y_oc
    x_oc = oci_qaylq(x_oc,y_oc)[0]
    y_oc = oci_qaylq(x_oc,y_oc)[1]
    
    #kapiki banan utely
    if x_monkey == x_banan_0 and y_monkey == y_banan_0:
        point += 1
        print (f'Point = {point} 🍌')
        if point == 5:
            print ("🫵 ~ WIN GAME !!!")   
            exit()         

    #banani hertakan haytnvelu vayry
    if point_0 < point: 
        map_x -= 1
        map_y -= 1
        x_banan_0 = random.randint(0,map_x-1)
        y_banan_0 = random.randint(0,map_y-1)
        point_0 = point
        if x_banan_0 == x_monkey:
            x_banan_0 = random.randint(0,map_x-1)
        elif y_banan_0 == y_monkey:
            y_banan_0 = random.randint(0,map_y)
    else:
        print (f'Point = {point} 🍌')

    #kyanqer   
    if x_monkey == -1 or x_monkey == map_x + 1 or y_monkey == -1 or y_monkey == map_y+1 or (x_oc == x_monkey and y_oc == y_monkey):
        kyanq -= 1
        print (f'Life = {kyanq} ❤️')
        if kyanq == 0:
            print ("🫵 ~ LOSE GAME LOSER !!!")
            exit()
    else:
        print (f'Life = {kyanq} ❤️')
    
    #vor het shprti kaktusi mej mtneluc heto
    #vor ocy kci shprti 0,0 
    if x_monkey == map_x + 1:
        x_monkey -= 1
    elif x_monkey == -1:
        x_monkey += 1
    elif y_monkey == map_y +1:
        y_monkey -= 1
    elif y_monkey == -1:
        y_monkey += 1
    elif x_monkey == x_oc and y_monkey == y_oc:
        x_monkey = 0
        y_monkey = 0
    #qartez
    for a in range(map_y+1,-2,-1):
        for a_0 in range(-1,map_x+2):
            #sahmanner
            if a == y_monkey and a_0 == x_monkey: # kapiki kordinatna
                print("🐒", end = '') 
            elif a == y_oc and a_0 == x_oc: #oci kordinatna
                print("🐍", end = '') 
            elif (a == map_y+1 or a == -1) or a_0 == map_x+1 or a_0 == -1 : #sahmannery
                print ("🌵", end = '')
            elif a == y_banan_0 and a_0 == x_banan_0 : #banani kordinat
                print("🍌", end = '')
            else:
                print("🌴", end = '')
        print()
    #karavarum
    print ("Control is (W,A,S,D)")
    step = msvcrt.getwch().lower()
    control = step
    n = 0
    #xaxic elq (enterov harmar cher miamit kpnuym ei dra hamar em 0 drel)
    if step == '0':
        break
    # haskanuma inch tar es mutq arel
    if step in ('w','a','s','d'):
        for step in ('w','a','s','d'):
            n += 1
            if control == step:
                break
        # haskanuma mutq aracd tary ur piti texapoxi kapikin
        if n == 1 and y_monkey != map_y+1:
            y_monkey += 1
        elif n == 2 and x_monkey != -1 :
            x_monkey -= 1
        elif n == 3 and y_monkey != -1 :
            y_monkey -= 1
        elif n == 4 and x_monkey != map_x+1:
            x_monkey += 1