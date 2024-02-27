### Rova
### Smart Cashier Program v. 1.0
import time
import random
import os
os.system('cls')
print('\n👋😄 Hello, I am the Smart Cashier created by #Rova to help you quickly understand.\nCan you provide your total amount using the specified quantity of coins with denominations of 1, 5, 10, 25?\n')

while True:
    print('To exit, simply press Enter without input.')
    text = input("Input amount(cent): ")
    
    if text == '':
        break
    
    n = int(input("Input quantity: "))
    amount = int(text)
    
    if (n != 0 and amount != 0) and n * 25 >= amount:
        print('Give me up to 5 seconds to think 🧐  ...')
    
    variants = []
    start_t = time.time()
    finish_t = start_t + 5
    
    while time.time()< finish_t:
        if amount == 0 or n == 0:
            break
        elif n * 25 < amount:
            break
        
        variant = []
        n_25 = random.randint(0,n)
        n_10 = random.randint(0,n)
        n_5 = random.randint(0,n)
        n_1 = random.randint(0,n) 
        if n_25*25 + n_10*10 + n_5*5 + n_1*1  == amount and n_1 + n_5 + n_10 + n_25 == n:
            variant.append(n_25)
            variant.append(n_10)
            variant.append(n_5)
            variant.append(n_1)
            if variant not in variants:
                variants.append(variant)
    
    if len(variants) == 0:
        print("😰 Sorry, but that's not possible.\n")
    else:
        variants.sort()
        print("🥳 Here's how you can optimally obtain your total!\n")
        print (f'25🪙  = {variants[-1][0]}\n10🪙  = {variants[-1][1]}\n 5🪙  = {variants[-1][2]}\n 1🪙  = {variants[-1][3]}\n')