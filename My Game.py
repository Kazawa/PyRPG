
#Game still needs a menu for explaining how to play at the start...


import random
from collections import Counter
import time
import sys
#Enemies = Enemy name [HP, Attack, Defense] - this is pointless atm, just need a list...
enemyDict = {'Goblin': [20, 2, 2],
             'Tree Trunk': [40, 4, 6],  
             'Penguini': [10, 1, 0]}

#These 4 lines take the keys (strings) from the dictionary and put it into a list so i can call random things from the list
enemyList = []

for k in sorted(enemyDict.keys()):
    enemyList.append(k)


#This is your player stats  - dictionary is not in use....
player = {'Playa': [100, 10, 10]}

playerHP = 100
playerAtk = 15
playerDef = 0
playerExp = 0

playerGold = 0

# - I'll need this later
'''
mylist = []

#This loop will generate random numbers within the range of 0-9 and add them to a list 100 times (as y dictates)
def first():
    y = 0
    while y < 100:
        x = (random.randint(0,9))
        y += 1
        mylist.append(x)
        print (x)
        print ('mylist: ', mylist)

#this will scan the list -mylist- and print how many of each item is in the list :)  make sure to import!
def second():
    a = dict(Counter(mylist))
    print (a)

first()
second()
'''
def fight():
    #Player Stats - I want this global for 'leveling up' purposes.
    global playerHP
    global playerAtk
    global playerDef
    global playerExp

    global playerGold
    
    enemy = random.choice(enemyList)
    #print('You have encountered a', enemy)
    time.sleep(0.75)
    if enemy == 'Goblin':
        #Goblin Stats
        goblinHP = 20
        goblinAtk = 2
        goblinDef = 2
        goblinExp = 220
        goblinGold = 50
        
        print ('You have encountered a Goblin!')
        while goblinHP > 0 and playerHP > 0:
            print ('------Player------''  ''------Goblin------')
            print ('[HP] :',playerHP,'        [HP] :', goblinHP)
            print ('[ATK]:',playerAtk,'          [ATK]:', goblinAtk)
            print ('[DEF]:',playerDef,'          [DEF]:', goblinDef)
            print ('[EXP]:',playerExp)
            print ('------------------------------------------')
            getKey = input('Type "a" for attack, "d" for defend: ')
            if getKey == 'a' or getKey == 'A':
                goblinHP -= playerAtk
                time.sleep(0.75)
                print ('***Goblin has taken', playerAtk, 'damage***')
                time.sleep(0.75)
                if goblinHP <= 0:
                    print(enemy, 'has been defeated.')
                    time.sleep(0.75)
                    print('~~/ You gained', goblinExp,'exp and', goblinGold, 'gold \~~')
                    playerExp += goblinExp
                    playerGold += goblinGold
                    levelUp()
                    break
                print ('***Goblin attacks dealing', goblinAtk, 'damage***')
                playerHP -= goblinAtk
                time.sleep(1)
                if playerHP < 0:
                    print('You\'re dead sucka!')
                    time.sleep(1)
                    print('GAME OVER')
                    sys.exit()
            elif getKey == 'd' or getKey == 'D':
                time.sleep(0.75)
                print('Player is defending,', enemy, 'attacks have no effect.')
                time.sleep(1)
      

    elif enemy == 'Tree Trunk':
        #Tree Trunk Stats
        treeTrunkHP = 30
        treeTrunkAtk = 5
        treeTrunkDef = 4
        treeTrunkExp = 360
        treeTrunkGold = 200
        
        print ('You have encountered a Tree Trunk!')
        while treeTrunkHP > 0 and playerHP > 0:
            print ('------Player------''  ''------Tree Trunk------')
            print ('[HP] :',playerHP,'        [HP] :', treeTrunkHP)
            print ('[ATK]:',playerAtk,'          [ATK]:', treeTrunkAtk)
            print ('[DEF]:',playerDef,'          [DEF]:', treeTrunkDef)
            print ('[EXP]:',playerExp)
            print ('------------------------------------------')
            getKey = input('Type "a" for attack, "d" for defend: ')
            if getKey == 'a' or getKey == 'A':
                treeTrunkHP -= playerAtk
                time.sleep(0.75)
                print ('***Tree Trunk has taken', playerAtk, 'damage***')
                time.sleep(0.75)
                if treeTrunkHP <= 0:
                    print(enemy, 'has been defeated.')
                    time.sleep(0.75)
                    print('~~/ You gained', treeTrunkExp,'exp and', treeTrunkGold, 'gold \~~')
                    playerExp += treeTrunkExp
                    playerGold += treeTrunkGold
                    levelUp()
                    break
                print ('***Tree Trunk attacks dealing', treeTrunkAtk, 'damage***')
                playerHP -= treeTrunkAtk
                time.sleep(1)
                if playerHP < 0:
                    print('You\'re dead sucka!')
                    time.sleep(1)
                    print('GAME OVER')
                    sys.exit()
            elif getKey == 'd' or getKey == 'D':
                time.sleep(0.75)
                print('Player is defending,', enemy, 'attacks have no effect.')
                time.sleep(1)

        
    elif enemy == 'Penguini':
        #Penguini Stats
        penguiniHP = 10
        penguiniAtk = 1
        penguiniDef = 0
        penguiniExp = 50
        penguiniGold = 25
        
        print ('You have encountered a Penguini!')
        while penguiniHP > 0 and playerHP > 0:
            print ('------Player------''  ''------Tree Trunk------')
            print ('[HP] :',playerHP,'        [HP] :', penguiniHP)
            print ('[ATK]:',playerAtk,'          [ATK]:', penguiniAtk)
            print ('[DEF]:',playerDef,'          [DEF]:', penguiniDef)
            print ('[EXP]:',playerExp)
            print ('------------------------------------------')
            getKey = input('Type "a" for attack, "d" for defend: ')
            if getKey == 'a' or getKey == 'A':
                penguiniHP -= playerAtk
                time.sleep(0.75)
                print ('***Penguini has taken', playerAtk, 'damage***')
                time.sleep(0.75)
                if penguiniHP <= 0:
                    print(enemy, 'has been defeated.')
                    time.sleep(0.75)
                    print('~~/ You gained', penguiniExp,'exp and', penguiniGold, 'gold \~~')
                    playerExp += penguiniExp
                    playerGold += penguiniGold
                    levelUp()
                    break
                print ('***Penguini attacks dealing', penguiniAtk, 'damage***')
                playerHP -= penguiniAtk
                time.sleep(1)
                if playerHP < 0:
                    print('You\'re dead sucka!')
                    time.sleep(1)
                    print('GAME OVER')
                    sys.exit()
            elif getKey == 'd' or getKey == 'D':
                time.sleep(0.75)
                print('Player is defending,', enemy, 'attacks have no effect.')
                time.sleep(1)
    
def movement():
    time.sleep(0.75)
    print('Walking')

def levelUp():
    global playerExp
    global playerGold
    while playerExp >= 100:
        playerExp = playerExp - 100
        time.sleep(0.75)
        print('new exp amount: ', playerExp)
        time.sleep(0.75)
        print('You have leveled up!')
        time.sleep(0.75)
        print('You have', playerGold, 'gold pieces.')

#This is for auto movement and random encounters - this also might be main....
def moveEnc():
    while True:
        battle = (random.randint(1, 14))
        if battle == 1 or battle == 5 or battle == 9:
            fight()
        else: #battle == 2 or battle == 3 or battle == 4 or battle == 6 or battle == 7 or battle == 8 or battle == 10 or battle == 11 or battle == 12 or battle == 13 or battle == 14:
            movement()
     
#def fightLoop():
    



moveEnc()
