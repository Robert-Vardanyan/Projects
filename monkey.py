### Rova
### Monkey_Game update!
### Monkey game v.2.1
### A new game with smart snake.
# Game features:
#   Exit ---> 0
#   The map decreases after earning points.
#   If the monkey touches a cactus or a snake, it loses a life.
#   The monkey can be controlled without pressing the Enter button.

import random
import msvcrt
import os
# Lives and points of the monkey.
kyanq = 3   
point = 0
point_0 = 0
# Map.
map_x = 30 #int(input("Input MAP(X) = ")) 
map_y = 30 #int(input("Input MAP(Y) = "))
# Appearance of the monkey's coordinates.
x_monkey = random.randint(0,map_x)
y_monkey = random.randint(0,map_y)
# Appearance of the snake's coordinates.
x_oc = map_x // 2
y_oc = map_y // 2
# Appearance of the banana coordinates taking into account the monkey's coordinates.
x_banan_0 = random.randint(0,map_x-1)
y_banan_0 = random.randint(0,map_y-1)
if x_banan_0 == x_monkey:
    x_banan_0 = random.randint(0,map_x-1)
if y_banan_0 == y_monkey:
    y_banan_0 = random.randint(0,map_y-1)
# Main program
while True:
    # Clearing the command line interface
    os.system('cls') 
    # Snake movement logic
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
    # The monkey eats the banana
    if x_monkey == x_banan_0 and y_monkey == y_banan_0:
        point += 1
        print (f'Point = {point} 🍌')
        if point == 5:
            print ("🫵 ~ WIN GAME !!!")   
            exit()         
    # The next appearance of the banana
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
    # Monkey's life points
    if x_monkey == -1 or x_monkey == map_x + 1 or y_monkey == -1 or y_monkey == map_y+1 or (x_oc == x_monkey and y_oc == y_monkey):
        kyanq -= 1
        print (f'Life = {kyanq} ❤️')
        if kyanq == 0:
            print ("🫵 ~ LOSE GAME LOSER !!!")
            exit()
    else:
        print (f'Life = {kyanq} ❤️')
    # Discards the monkey if it touches a cactus or a snake
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
    # Map generation
    for a in range(map_y+1,-2,-1):
        for a_0 in range(-1,map_x+2):
            # Objects on the map
            if a == y_monkey and a_0 == x_monkey: # Monkey
                print("🐒", end = '') 
            elif a == y_oc and a_0 == x_oc: # Snake
                print("🐍", end = '') 
            elif (a == map_y+1 or a == -1) or a_0 == map_x+1 or a_0 == -1 : # Cacti around the perimeter
                print ("🌵", end = '')
            elif a == y_banan_0 and a_0 == x_banan_0 : # Banana
                print("🍌", end = '')
            else:
                print("🌴", end = '') # Trees
        print()
    # Control
    print ("Control is (W,A,S,D)")
    step = msvcrt.getwch().lower()
    control = step
    n = 0
    # Exit from the game
    if step == '0':
        break
    # Understanding which button is pressed
    if step in ('w','a','s','d'):
        for step in ('w','a','s','d'):
            n += 1
            if control == step:
                break
        # Understanding where to move after pressing the button
        if n == 1 and y_monkey != map_y+1:
            y_monkey += 1
        elif n == 2 and x_monkey != -1 :
            x_monkey -= 1
        elif n == 3 and y_monkey != -1 :
            y_monkey -= 1
        elif n == 4 and x_monkey != map_x+1:
            x_monkey += 1