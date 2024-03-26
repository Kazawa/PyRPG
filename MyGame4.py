
import random
from collections import Counter
import time
import sys

playername = input ('Name your character: ')

inventory = ['Potion',
             'Potion',
             'Potion',
             'Antidote']

shopItems = ['Potion',
             'Antidote']

class Player:
    def __init__(self, name, HP, STR, DEF, EXP, GOLD, LEVEL):
        self.playername = name
        self.hp = HP
        self.strength = STR
        self.defense = DEF
        self.exp = EXP
        self.gold = GOLD
        self.level = LEVEL

Player1 = Player(playername, 100, 5, 1, 0, 0, 1)

class Enemies:
    enemyList = ['Goblin',
                 'Tree Trunk',
                 'Penguini',
                 'Killer Frog',
                 'Maneater']

    def __init__(self, name, HP, STR, DEF, EXP, GOLD):
        self.enname = name
        self.enhp = HP
        self.enstr = STR
        self.endef = DEF
        self.enexp = EXP
        self.engold = GOLD

def fight():
    
    enemy = random.choice(Enemies.enemyList)
    
    if enemy == 'Goblin':
        currentMonster = Enemies('Goblin', 20, 5, 3, 30, 25)
    elif enemy == 'Tree Trunk':
        currentMonster = Enemies('Tree Trunk', 30, 5, 4, 65, 75)
    elif enemy == 'Penguini':
        currentMonster = Enemies('Penguini', 10, 2, 0, 15, 10)
    elif enemy == 'Killer Frog':
        currentMonster = Enemies('Killer Frog', 20, 3, 1, 15, 40)
    elif enemy == 'Man Eater':
        currentMonster = Enemies('Man Eater', 60, 8, 4, 75, 125)
        
    while currentMonster.enhp > 0 and Player1.hp > 0:
        print ('---------------------------------------------')
        print ('|--', Player1.playername, '[LVL] [', Player1.level,']---''  ''---', currentMonster.enname, '--|')
        print ('---------------------------------------------')
        print ('[HP] :',Player1.hp,'          [HP] :', currentMonster.enhp)
        print ('[ATK]:',Player1.strength,'          [ATK]:', currentMonster.enstr)
        print ('[DEF]:',Player1.defense,'           [DEF]:', currentMonster.endef)
        print ('------------------------------------------')
        print ('[EXP]:',Player1.exp, '    [GOLD]:', Player1.gold)
        print ('------------------------------------------')
        getKey = input('Battle Command: ')
        if getKey == 'a' or getKey == 'A':
            enemyHP -= Player1.strength
            time.sleep(0.75)
            print ('***', enemy, 'has taken', Player1.strength, 'damage***')
            time.sleep(0.75)
            if enemyHP <= 0:
                print(enemy, 'has been defeated.')
                time.sleep(0.75)
                print('~~/ You gained', enemyExp,'exp and', enemyGold, 'gold \~~')
                Player1.exp += enemyExp
                Player1.gold += enemyGold
                levelUp()
                break
            print ('***', enemy, 'attacks dealing', enemyAtk, 'damage***')
            Player1.hp -= enemyAtk
            time.sleep(1)
            if Player1.hp < 0:
                print('You\'re dead sucka!')
                time.sleep(1)
                print('GAME OVER')
                sys.exit()
        elif getKey == 'd' or getKey == 'D':
            time.sleep(0.75)
            print('Player is defending,', enemy, 'attacks have no effect.')
            time.sleep(1)
        elif getKey == 'r' or getKey == 'R':
            run = random.randint(1, 5)
            if run == 5:
                time.sleep(0.75)
                print ('You were able to escape!')
                break
            else:
                time.sleep(0.75)
                print('You were unable to escape')
                time.sleep(0.75)
                print ('***', enemy, 'attacks dealing', enemyAtk, 'damage***')
                Player1.hp -=enemyAtk
                time.sleep(0.75)
            
#This is part of the main loop used for auto-movement 
def movement():
    time.sleep(0.75)
    getKey = input('Exploring...: ')
    if getKey == 'i' or getKey == 'I':
        openInventory()
    elif getKey == 's' or getKey == 'S':
        openShop()
    treasure()

def treasure():
    treasure = random.randint(1, 20)
    if treasure == 1:
        time.sleep(0.75)
        print ('You found a Potion!')
        inventory.append('Potion')
    
    elif treasure == 2:
        time.sleep(0.75)
        print ('You found an Antidote!')
        inventory.append('Antidote')

def openShop(): #this is a little broken when you can afford things it loops too many times...
    print('')
    print('``````Welcome to the Shop!`````` "x" to Exit.')
    print('`                              `')
    print('`       [Items for Sale]       `')
    print('`                              `')
    print('`  - Potion: 200G -            `')
    print('`  - Antidote: 1000G -         `')
    print('================== Gold: ', Player1.gold)
    print('')
    while True: 
        getKey = input ('What would you like to buy?: ')
        if getKey in shopItems:
            while True:
                try:
                    qty = int(input('How many?: '))
                    if getKey == 'Potion':
                        cost = 200
                        totalCost = cost * qty
                        if Player1.gold < totalCost:
                            amtShort = totalCost - Player1.gold
                            print('Sorry you are', amtShort, 'gold short.')
                            break
                        elif Player1.gold >= totalCost:
                            Player1.gold -= totalCost
                            x = qty
                            while x > 0:
                                inventory.append(getKey)
                                x -= 1
                        time.sleep(0.75)    
                        print('You bought', qty, getKey)
                        time.sleep(0.75)
                        print('~~~You now have', Player1.gold, 'gold.~~~')
                        time.sleep(0.75)
                        break
                    if getKey == 'Antidote':
                        cost = 1000
                        totalCost = cost * qty
                        if Player1.gold < totalCost:
                            amtShort = totalCost - Player1.gold
                            print('Sorry you are', amtShort, 'gold short.')
                            break
                        elif Player1.gold >= totalCost:
                            Player1.gold -= totalCost
                            x = qty
                            while x > 0:
                                inventory.append(getKey)
                                x -= 1
                        time.sleep(0.75)    
                        print('You bought', qty, getKey)
                        time.sleep(0.75)
                        print('~~~You now have', Player1.gold, 'gold.~~~')
                        time.sleep(0.75)
                        break
                except ValueError:
                    print('Please input a number.')
        elif getKey == 'x' or getKey == 'X':
            time.sleep(0.75)
            print('```Thank you for shopping with us!```')
            break
        
def openInventory(): #need a better loop for this like the openShop
    while True:
        a = dict(Counter(inventory))
        print('')
        print ('``````Your inventory``````')
        print('')
        print (a)
        print('')
        getKey = input ('What item would you like to use?: ')
        if getKey in inventory:
            time.sleep(0.75)
            inventory.remove(getKey)
            if getKey == 'Potion':
                Player1.hp += 25
            print ('You used one', getKey)
        else:
            print('```Exiting```')
            break
        
#This is the Level Up check script
def levelUp():
    while Player1.exp >= 100:
        Player1.exp = Player1.exp - 100
        time.sleep(0.75)
        print('You have leveled up!')
        Player1.level += 1
        time.sleep(0.75)
        Player1.hp += random.randint(20, 40)
        Player1.strength += random.randint(2, 5)
        Player1.defense += random.randint(0, 2)

#This is for auto movement and random encounters - this also might be main....
def moveEnc():
    while True:
        battle = (random.randint(1, 14))
        if battle == 1 or battle == 5 or battle == 9:
            fight()
        else: #battle == 2 or battle == 3 or battle == 4 or battle == 6 or battle == 7 or battle == 8 or battle == 10 or battle == 11 or battle == 12 or battle == 13 or battle == 14:
            movement()

def mainMenu():
    print('---------------------------------------------------')
    print('                Thrill of the Kill!                ')
    print('                               ')
    print('                               ')
    print(' General Info                  ')
    print(' *Your goal is to beat the Boss')
    print(' *Push Enter to Explore')
    print(' *Follow the simple prompts to attack and defend')
    print(' *This is an RPG type game with random encounters,')
    print(' experience points, leveling up, and loot.')
    print(' *You level up every 100 exp gained.')
    print(' *There is no story though really, because who reads?')
    print(' *Coded by Kazawa')
    print('---------------------------------------------------')
    print('TODO: add shop, add better system tracking for player')
    print('stats and leveling up, more complicated damage system')
    print('that will take defensive value into account, dodge atks, add equipment')
    print('maybe add a way to save/load progress...,')
    print('tracking statistics: enemies defeated, steps taken, damage delt, damage taken, etc.')
    print('A skill systemwhere the more you use a skill the stronger it gets.')
    print('          Instructions')
    print('                      ')
    print('When in battle type "a" to attack, "d" to defend, and "r" to try to run')
    print('When exploring type "i" to access your inventory, [enter] or x to leave it')
    print('When explortin type "s" to access the shop and "x" to leave the shop')
    print('__You must print the item you wish to use exactly as listed: Potion (capitol P) ')
    print('Kill Things!')
    print('')
    
mainMenu()
moveEnc()

#the green was right below:
#enemy = random.choice(Enemies.enemyList)
#in the fight() function
#finally got the class for enemies working, this can be deleted when i feel ready....
'''
    #print('You have encountered a', enemy)
    time.sleep(0.75)
    if enemy == 'Goblin':
        #Goblin Stats
        enemyHP = 2045678
        enemyAtk = 54678
        enemyDef = 34678
        enemyExp = 304678
        enemyGold = (random.randint(20, 30))
        print ('You have encountered a Goblin!')
        time.sleep(1)
      
    elif enemy == 'Tree Trunk':
        #Tree Trunk Stats
        enemyHP = 30
        enemyAtk = 5
        enemyDef = 4
        enemyExp = 65
        enemyGold = (random.randint(40, 75))     
        print ('You have encountered a Tree Trunk!')
        time.sleep(1)
        
    elif enemy == 'Penguini':
        #Penguini Stats
        enemyHP = 10
        enemyAtk = 1
        enemyDef = 0
        enemyExp = 10
        enemyGold = (random.randint(10, 15))  
        print ('You have encountered a Penguini!')
        time.sleep(1)

    elif enemy == 'Killer Frog':
        #Frog Stats
        enemyHP = 20
        enemyAtk = 2
        enemyDef = 1
        enemyExp = 15
        enemyGold = (random.randint(35, 50))
        print('You have encountered a Killer Frog!')
        time.sleep(1)

    elif enemy == 'Maneater':
        #Maneater Stats
        enemyHP = 60
        enemyAtk = 8
        enemyDef = 4
        enemyExp = 75
        enemyGold = (random.randint(100, 200))
        print('You have encountered a Maneater')
        time.sleep(1)
'''
