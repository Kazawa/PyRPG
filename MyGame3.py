
import random
from collections import Counter
import time
import sys

getPlayerName = input ('Name your character: ')

enemyList = ['Goblin',
             'Tree Trunk',
             'Penguini',
             'Killer Frog',
             'Maneater']

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

Player1 = Player(getPlayerName, 100, 5, 1, 0, 0, 1)

print(Player1.hp)
print(Player1.strength)
print(Player1.defense)
print(Player1.exp)
print(Player1.gold)
print(Player1.level)


#these stats are being replaced by a class 
playerHP = 100
playerAtk = 15
playerDef = 0
playerExp = 0
playerGold = 6000
playerLevel = 1 #for later


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
        enemyHP = 20
        enemyAtk = 5
        enemyDef = 3
        enemyExp = 30
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

    while enemyHP > 0 and Player1.hp > 0:
        print ('---------------------------------------------')
        print ('|--', Player1.playername, '[LVL] [', Player1.level,']---''  ''---', enemy, '--|')
        print ('---------------------------------------------')
        print ('[HP] :',Player1.hp,'          [HP] :', enemyHP)
        print ('[ATK]:',Player1.strength,'          [ATK]:', enemyAtk)
        print ('[DEF]:',Player1.defense,'           [DEF]:', enemyDef)
        print ('------------------------------------------')
        print ('[EXP]:',Player1.exp, '    [GOLD]:', Player1.gold)
        print ('------------------------------------------')
        getKey = input('Battle Command: ')
        if getKey == 'a' or getKey == 'A':
            bonus = random.randint(2,4)
            print(bonus)
            enemyHP -= playerAtk * bonus
            time.sleep(0.75)
            print ('***', enemy, 'has taken', playerAtk, 'damage***')
            time.sleep(0.75)
            if enemyHP <= 0:
                print(enemy, 'has been defeated.')
                time.sleep(0.75)
                print('~~/ You gained', enemyExp,'exp and', enemyGold, 'gold \~~')
                playerExp += enemyExp
                playerGold += enemyGold
                levelUp()
                break
            print ('***', enemy, 'attacks dealing', enemyAtk, 'damage***')
            playerHP -= enemyAtk
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
                playerHP -=enemyAtk
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
    global playerGold
    print('')
    print('``````Welcome to the Shop!`````` "x" to Exit.')
    print('`                              `')
    print('`       [Items for Sale]       `')
    print('`                              `')
    print('`  - Potion: 200G -            `')
    print('`  - Antidote: 1000G -         `')
    print('================== Gold: ', playerGold)
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
                        if playerGold < totalCost:
                            amtShort = totalCost - playerGold
                            print('Sorry you are', amtShort, 'gold short.')
                            break
                        elif playerGold >= totalCost:
                            playerGold -= totalCost
                            x = qty
                            while x > 0:
                                inventory.append(getKey)
                                x -= 1
                        time.sleep(0.75)    
                        print('You bought', qty, getKey)
                        time.sleep(0.75)
                        print('~~~You now have', playerGold, 'gold.~~~')
                        time.sleep(0.75)
                        break
                    if getKey == 'Antidote':
                        cost = 1000
                        totalCost = cost * qty
                        if playerGold < totalCost:
                            amtShort = totalCost - playerGold
                            print('Sorry you are', amtShort, 'gold short.')
                            break
                        elif playerGold >= totalCost:
                            playerGold -= totalCost
                            x = qty
                            while x > 0:
                                inventory.append(getKey)
                                x -= 1
                        time.sleep(0.75)    
                        print('You bought', qty, getKey)
                        time.sleep(0.75)
                        print('~~~You now have', playerGold, 'gold.~~~')
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
        global playerHP
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
                playerHP += 25
            print ('You used one', getKey)
        else:
            print('```Exiting```')
            break
        
#This is the Level Up check script
def levelUp():
    global playerExp
    global playerGold
    global playerLevel
    while playerExp >= 100:
        playerExp = playerExp - 100
        time.sleep(0.75)
        print('You have leveled up!')
        playerLevel += 1
        time.sleep(0.75)

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
