#My RPG Game [Version 0.53]

import random
from collections import Counter
import time
import sys

#This needs to be put somewhere better/coded better
playername = input ('Name your character: ')

#These lists contain your player inventory and shop inventory
inventory = ['Potion',
             'Potion',
             'Potion',
             'Antidote']

shopItems = ['Potion',
             'Antidote']

#This is your player class.
class Player:
    def __init__(self, name, HP, HPMAX, STR, DEF, EXP, EXPMAX, GOLD, LEVEL):
        self.playername = name
        self.hp = HP
        self.maxhp = HPMAX
        self.strength = STR
        self.defense = DEF
        self.exp = EXP
        self.expmax = EXPMAX
        self.gold = GOLD
        self.level = LEVEL

#Player class objects
Player1 = Player(playername, 100, 100, 5, 1, 0, 100, 6660, 1)

#This is your enemy classs
class Enemies:
    enemyList = []

    def __init__(self, name, HP, STR, DEF, EXP, GOLD):
        self.enname = name
        self.enhp = HP
        self.enstr = STR
        self.endef = DEF
        self.enexp = EXP
        self.engold = GOLD
        
#Enemy class objecsts
#The enemyList is populated this way to avoid any crashes spelling errors might cause in enemyList
#while running the fight() function ect.
currentMonster = Enemies('Goblin', 20, 5, 3, 300, 25)
Enemies.enemyList.append(currentMonster.enname)
currentMonster = Enemies('Tree Trunk', 30, 5, 4, 650, 75)
Enemies.enemyList.append(currentMonster.enname)
currentMonster = Enemies('Penguini', 10, 2, 0, 150, 10)
Enemies.enemyList.append(currentMonster.enname)
currentMonster = Enemies('Killer Frog', 20, 3, 1, 150, 40)
Enemies.enemyList.append(currentMonster.enname)
currentMonster = Enemies('Man Eater', 60, 8, 4, 750, 125)
Enemies.enemyList.append(currentMonster.enname)

#This is a class to track various game statistics
class Stats:
    def __init__(self, distance, damageGiven, damageTaken, enemiesDefeated):
        self.distance = distance
        self.damageGiven = damageGiven
        self.damageTaken = damageTaken
        self.enemiesDefeated = enemiesDefeated

#This is the Stats class object
statCount = Stats(0, 0, 0, 0)

#This is the main battle loop 
def fight():

    randEnemy = random.choice(Enemies.enemyList)
    
    if randEnemy == 'Goblin':
        currentMonster = Enemies('Goblin', 20, 5, 3, 300, 25)
    elif randEnemy == 'Tree Trunk':
        currentMonster = Enemies('Tree Trunk', 30, 5, 4, 650, 75)
    elif randEnemy == 'Penguini':
        currentMonster = Enemies('Penguini', 10, 2, 0, 150, 10)
    elif randEnemy == 'Killer Frog':
        currentMonster = Enemies('Killer Frog', 20, 3, 1, 150, 40)
    elif randEnemy == 'Man Eater':
        currentMonster = Enemies('Man Eater', 60, 8, 4, 750, 125)
        
    while currentMonster.enhp > 0 and Player1.hp > 0:  #I think there should be playerTurn() and enemyTurn() functions created.... maybe not though...
        print ('---------------------------------------------')
        print ('|--', Player1.playername, '[LVL] [', Player1.level,']---''  ''---', currentMonster.enname, '--|')
        print ('---------------------------------------------')
        print ('[HP] :',Player1.hp, '/', Player1.maxhp, '             [HP] :', currentMonster.enhp)
        print ('[ATK]:',Player1.strength,'               [ATK]:', currentMonster.enstr)
        print ('[DEF]:',Player1.defense,'               [DEF]:', currentMonster.endef)
        print ('------------------------------------------')
        print ('[EXP]:',Player1.exp, '/', Player1.expmax, '    [GOLD]:', Player1.gold)
        print ('------------------------------------------')
        getKey = input('Battle Command: ').lower()
        if getKey == 'a' or getKey == 'A':
            currentMonster.enhp -= Player1.strength
            statCount.damageGiven += Player1.strength
            time.sleep(0.75)
            print ('***', currentMonster.enname , 'has taken', Player1.strength, 'damage***')
            time.sleep(0.75)
            if currentMonster.enhp <= 0:
                print(currentMonster.enname, 'has been defeated.')
                statCount.enemiesDefeated += 1
                time.sleep(0.75)
                print('~~/ You gained', currentMonster.enexp,'exp and', currentMonster.engold, 'gold \~~')
                Player1.exp += currentMonster.enexp
                Player1.gold += currentMonster.engold
                levelUp()
                break
            print ('***', currentMonster.enname, 'attacks dealing', currentMonster.enstr, 'damage***')
            Player1.hp -= currentMonster.enstr
            statCount.damageTaken += currentMonster.enstr
            time.sleep(1)
            if Player1.hp < 0:
                print('You\'re dead sucka!')
                time.sleep(1)
                print('GAME OVER')
                sys.exit()
        elif getKey == 'd' or getKey == 'D':
            time.sleep(0.75)
            print('Player is defending,', currentMonster.enname, 'attacks have no effect.')
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
                print ('***', currentMonster.enname, 'attacks dealing', currentMonster.enstr, 'damage***')
                Player1.hp -=currentMonster.enstr
                time.sleep(0.75)
            
#Movement is the exploring loop/function 
def movement():
    time.sleep(0.75)
    getKey = input('Exploring...: ')
    if getKey == 'i' or getKey == 'I':
        openInventory()
    elif getKey == 's' or getKey == 'S':
        openShop()
    elif getKey == 'stats' or getKey == 'Stats':
        displayStats()  
    treasure()
    statCount.distance += 1

#Stats function
def displayStats():
    print('=========== STATS =============')
    print('')
    print('Total Steps Taken: ', statCount.distance)
    print('Total Enemies Defeated: ', statCount.enemiesDefeated)
    print('Total Damage Dealt: ', statCount.damageGiven)
    print('Total Damage Received: ', statCount.damageTaken)
    print('')
    print('===============================')

#Treasure randomly find the player treasure while exploring
def treasure():
    treasure = random.randint(1, 21)
    if treasure == 1:
        time.sleep(0.75)
        print ('You found a Potion!')
        inventory.append('Potion')
    
    elif treasure == 2:
        time.sleep(0.75)
        print ('You found an Antidote!')
        inventory.append('Antidote')

#This is the shop loop - i think we can make this shorter... 
def openShop():
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
        
#This is the inventory loop - need a better loop for this like the openShop, need more feedback for player        
def openInventory(): 
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
        
#This is the Level Up check script - need more feedback for player
def levelUp():
    while Player1.exp >= Player1.expmax:
        newMaxHP = 0
        newMaxSTR = 0
        newMaxDEF = 0
        Player1.exp -= Player1.expmax
        Player1.expmax += 100
        time.sleep(0.75)
        print('You have leveled up!')
        Player1.level += 1
        time.sleep(0.75)
        newMaxHP += random.randint(20, 40)
        Player1.maxhp += newMaxHP
        Player1.hp = Player1.maxhp
        newMaxSTR += random.randint(3, 5)
        Player1.strength += newMaxSTR
        newMaxDEF += random.randint(0, 3)
        Player1.defense += newMaxDEF
        print('You have gained', newMaxHP, 'HP, ', newMaxSTR, 'STR, and ', newMaxDEF, 'DEF.')
        
#This function decides if there will be a battle or exploring and is the main loop.
def moveEnc():
    while True:
        battle = (random.randint(1, 14))
        if battle == 1 or battle == 5 or battle == 9:
            fight()
        else:
            movement()

#This is your main menu - needs work. Possible load game option... :)
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
    print(' *You level up at increased intervals')
    print(' *There is no story though, really, because who reads?')
    print(' *Coded by Kazawa')
    print('---------------------------------------------------')
    print('TODO: more complicated damage system')
    print('that will take defensive value into account, dodge atks, miss atks, add equipment')
    print('maybe add a way to save/load progress...,')
    print('A skill system where the more you use a skill the stronger it gets.')
    print('---------------------------------------------------')
    print('          Instructions')
    print('---------------------------------------------------')
    print('When in battle type "a" to attack, "d" to defend, and "r" to try to run')
    print('When exploring type "i" to access your inventory, [enter] or x to leave it')
    print('When exploring type "s" to access the shop and "x" to leave the shop')
    print('When exploring type "stats" to view various gameplay stats')
    print('__You must print the item you wish to use exactly as listed: Potion (capital P) ')
    print('Kill Things!')
    print('')
    
    
mainMenu()
moveEnc()
