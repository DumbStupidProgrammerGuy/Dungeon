import main # replace with api filename
import random
import getch
import curses
import time
from IPython.display import display, Image, HTML, Markdown
# import tkinter as tk
# from tkinter import font

window = curses.initscr()
window.nodelay(True)
curses.noecho()

enemyTypes=[
    # "Dungeon Lizard",
    "Enemy"
    # "slime"
    ]


slimeSprites = [
    "(\u0c77 \u0D2E \u0c84)", 
    "(\u0c77  \u0c84)", 
    "(\u0c77 \U00010119 \u0c84)", 
    "(\u0c77 \U00011119 \u0c84)", 
    "(\u0c77 \U00010101 \u0c84)",
    "(\U00010F57 \U00011119 \U00010F57)", 
    "(\U00010F57 \U00010119 \U00010F57)", 
    "(\U00010F57 \U00010101 \U00010F57)", 
    "( \U00010F58 )"
    ]

slimeColors  = [
    "\033[32m", # Green
    "\033[34m", # Blue
    "\033[35m" # Purple
]

lizardColors  = [
    "\033[32m", # Green
    "\033[32m", # Green
    "\033[32m", # Green
    "\033[32m", # Green
    "\033[32m", # Green
    "\033[33m", # Orange
    "\033[33m", # Orange
    "\033[33m", # Orange
    "\033[34m", # Blue
    "\033[34m", # Blue
    "\033[35m" # Purple
]

enemySprites = [
    "\U00013020",
    "\U0001301A",
    "\U0001301B",
    "\U0001301C",
    "\U0001301D",
    "\U0001301E",
    "\U0001301F",
    "\U00013041"
]

actions={
    "Attack":"target.takeDamage(self.damageMod)",
    "Defend":"self.defense += self.defenseMod",
    "Warrior's Strike":"target.takeDamage(self.damageMod+1)",
    "Warrior's Defense":"self.defense += self.defenseMod+1",
    "Shield Bash" : "target.takeDamage(self.damageMod//2)",
    "Sword Slash":"for enemy in enemies: enemy.takeDamage(self.damageMod//2 +1)",
    "Cunning Strike": "target.takeDamage(self.damageMod+1)",
    "Desperate Dodge": "self.dodges += 3",
    "Enhanced Relexes": "self.dodgeChance += 25",
    "Counterstrike": "self.counterstriking = True",
    "Dodge": "self.dodges += 1",
    "Split":'self.splitting = True',
    "Ooze": "target.takeDamage(target.defense + self.health//5, True)"
    }


cardsWithTargets=[
    "Attack",
    "Warrior's Strike",
    "Shield Bash",
    "Cunning Strike"]

items = [
    "Warrior's Sword",
    "Warrior's Shield",
    "Slink's Daggers",
    "Slink's Hood",
    "Mage's Spellbook",
    "Mage's Staff",
    "Weathered Sword",
    "Weathered Sheild",
    "Weathered Daggers",
    "Tattered Hood",
    "Tattered Spellbook",
    "Battered Staff",
    "Broken Sword",
    "Broken Shield",
    "Broken Daggers",
    "Torn Hood",
    "Torn Spellbook",
    "Broken Staff"
]

weapons = [
    "Warrior's Sword",
    "Slink's Daggers",
    "Mage's Staff",
    "Weathered Sword",
    "Weathered Daggers",
    "Battered Staff",
    "Broken Sword",
    "Broken Daggers",
    "Broken Staff"
]

nonWeaponItems = [
    "Warrior's Shield",
    "Slink's Hood",
    "Mage's Spellbook",
    "Weathered Sheild",
    "Tattered Hood",
    "Tattered Spellbook",
    "Broken Shield",
    "Torn Hood",
    "Torn Spellbook"
]

itemAbilities = {
    "Warrior's Sword" : "if self.damageMod < 5: self.damageMod = 5",
    "Warrior's Shield" : "if self.defenseMod < 5: self.defenseMod = 5",
    "Slink's Daggers" : "if self.damageMod < 4: self.damageMod = 4",
    "Slink's Hood" : "self.handSize = random.randrange(4, 6)",
    "Mage's Spellbook" : "",
    "Mage's Staff" : "if self.damageMod < 2: self.damageMod = self.defenseMod = 2",
    "Weathered Sword" : "if self.damageMod < 5: self.damageMod = 5",
    "Weathered Sheild" : "if self.defenseMod < 5: self.defenseMod = 5",
    "Weathered Daggers" : "if self.damageMod < 4: self.damgeMod = 4",
    "Tattered Hood" : "self.handSize = random.randrange(3, 5)",
    "Tattered Spellbook" : "",
    "Battered Staff" : "if self.damageMod < 2: self.damageMod = self.defenseMod = 2",
    "Broken Sword" : "if self.damageMod < 4: self.damgeMod = 4",
    "Broken Shield" : "",
    "Broken Daggers" : "if self.damageMod < 3: self.damageMod = 3",
    "Torn Hood" : "self.handSize = random.randrange(3, 4)",
    "Torn Spellbook" : "",
    "Broken Staff" : "if self.damageMod < 2: self.damageMod = self.defenseMod = 2"
}

itemDescriptions ={
    "Warrior's Sword" : "Increases your attack damage to 5",
    "Warrior's Shield" : "Increases your block amount to 5",
    "Slink's Daggers" : "Increases your attack damage to 4",
    "Slink's Hood" : "Increases your hand size to a random value between 4 and 6",
    "Mage's Spellbook" : "This item's ability hasn't been implemented yet, sorry", # Not implemented!
    "Mage's Staff" : "Increases your attack damage and block amount to 2",
    "Weathered Sword" : "Increases your attack damage to 5",
    "Weathered Sheild" : "Increases your block amount to 5",
    "Weathered Daggers" : "Increases your attack damage to 4",
    "Tattered Hood" : "Sets your hand size to a random value between 3 and 5",
    "Tattered Spellbook" : "This item's ability hasn't been implemented yet, sorry", # Not implemented!
    "Battered Staff" : "Increases your attack damage and block amount to 2",
    "Broken Sword" : "Increases your attack damage to 4",
    "Broken Shield" : "This item's ability hasn't been implemented yet, sorry", # Not implemented!
    "Broken Daggers" : "Increases your attack damage to 3",
    "Torn Hood" : "Has a 50\u0025 of increasing your hand size to 4",
    "Torn Spellbook" : "This item's ability hasn't been implemented yet, sorry", # Not implemented!
    "Broken Staff" : "Increases your attack damage and block amount to 2"
}

agedItem = {
    "Warrior's Sword" : "Weathered Sword",
    "Warrior's Shield" : "Weathered Sheild",
    "Slink's Daggers" : "Weathered Daggers",
    "Slink's Hood" : "Tattered Hood",
    "Mage's Spellbook" : "Tattered Spellbook",
    "Mage's Staff" : "Battered Staff",
    "Weathered Sword" : "Broken Sword",
    "Weathered Sheild" : "Broken Shield",
    "Weathered Daggers" : "Broken Daggers",
    "Tattered Hood" : "Torn Hood",
    "Tattered Spellbook" : "Torn Spellbook",
    "Battered Staff" : "Broken Staff",
    "Broken Sword" : None,
    "Broken Shield" : None,
    "Broken Daggers" : None,
    "Torn Hood" : None,
    "Torn Spellbook" : None,
    "Broken Staff" : None
}


class Player():
    def __init__(self, archetype = None):
        self.archetype = archetype
        self.floor = 1
        self.room = 1
        self.items = []
        self.deck = ["Attack", "Attack", "Attack"]
        self.discard = []
        self.maxHealth = 100
        self.defense = 0
        self.handSize = 3
        self.damageMod = 1
        self.defenseMod = 1
        self.defaultDodge = 0
        self.dodgeChance = 0
        self.dodges = 0
        self.hand = []
        self.counterstriking = False
        self.cardDescriptions = {
            "Attack" : f"Deal {self.damageMod} damage to target enemy",
            "Defend" : f"Block {self.defenseMod} damage on the enemy's next turn",
            "Warrior's Strike" : f"Deal {self.damageMod+1} damage to target enemy",
            "Warrior's Defense" : f"Block {self.defenseMod+1} damage on the enemy's next turn",
            "Shield Bash" : f"Deal damage to target enemy equal to 2x your defense ({self.defense*2})",
            "Sword Slash" : f"Deal {self.damageMod//2} damage to ALL enemies"
        }
        if self.archetype == "Warrior":
            self.deck.append("Warrior's Strike")
            self.deck.append("Warrior's Defense")
            self.deck.append("Shield Bash")
            self.deck.append("Sword Slash")
            self.items.append("Warrior's Sword")
            self.items.append("Warrior's Shield")
            self.maxHealth = 100
        elif self.archetype == "Slink":
            self.deck.append("Cunning Strike")
            self.deck.append("Desperate Dodge")
            self.deck.append("Enhanced Relexes")
            # self.deck.append("Counterstrike")
            self.items.append("Slink's Daggers")
            self.items.append("Slink's Hood")
            self.deck.append("Dodge")
            self.deck.append("Dodge")
            self.deck.append("Dodge")
            self.defaultDodge = 25
            self.maxHealth = 80
            
        elif self.archetype == "Mage":
            self.deck.append("Careful Strike")
            self.deck.append("Precise Defense")
            self.deck.append("Incantation")
            self.deck.append("Divination")
            self.items.append("Mage's Spellbook")
            self.items.append("Mage's Staff")
            self.maxHealth = 90
        
        if not self.archetype == "Slink":
            self.deck.append("Defend")
            self.deck.append("Defend")
            self.deck.append("Defend")
        self.health = self.maxHealth

    def putChamp(self):
        main.putChamp(self.room, ", ".join(self.deck), ", ".join(self.items))
    
    def  die(self):
        print("You died!")
        if self.floor < 10:
            main.putDead(self.floor, self.room, ", ".join(self.items))
        else:
            main.putChamp(self.room, ", ".join(self.deck), ", ".join(self.items))

    def takeDamage(self, amount, ooze = False):
        if self.dodges > 0 or random.randrange(1, 100) <= self.dodgeChance:
            if self.dodges > 0:
                self.dodges -= 1
            if ooze:
                print("The slime's ooze can't be dodged!")
            else:
                print("You dodged the attack!")
        else:
            damageTaken = amount - self.defense
            if damageTaken < 0:
                damageTaken = 0
            self.health -= damageTaken
            damageBlocked = amount - damageTaken
            message = ""
            if ooze:
                print("The slime's ooze went through your block!")
                time.sleep(1)
            elif self.defense > 0:
                message = f"blocked {self.defense} damage and"            
            time.sleep(1)
            print(f'You {message} took {damageTaken} damage')
            time.sleep(1)
            if self.health <= 0:
                if self.floor == 10:
                    self.putChamp()
                elif 1 <= self.floor <= 9:
                    self.die()
        if self.counterstriking:
            print("Counterstiking hasn't been implemented yet, sorry. :(")
            self.counterstriking = False

    def enterRoom(self, floor, room):
        self.dodgeChance = self.defaultDodge
        print(f"Entering floor {floor}, room {room}...")
        time.sleep(5)
        self.floor = floor
        self.room = room
        r = random.randrange(0, 3)
        r = 1
        # r = 0
        # r = 3
        # main.putDead(self.floor, self.room, self.archetype, ", ".join(self.deck),  ", ".join(self.items))
        message = ""
        for i in range(r):
            enemy = Enemy(random.choice(enemyTypes))
            enemies.append(enemy)
            if i == 0:
                message = f"A(n) {enemy.name}"
            if r > 1:
                if i == r-1 and i > 0:
                    message = message + f" and a {enemy.name} appeared!"
                else:
                    message = message + f", a {enemy.name}"
            else:
                message = message + " appeared!"


        if len(enemies) > 0:
            print(message)
            time.sleep(2)
            self.turn()
        else:
            print("There was nothing there.")
            time.sleep(1)
            if self.health < self.maxHealth:
                healAmount = self.maxHealth//10
                healthMissing = self.maxHealth - self.health
                if healAmount > healthMissing:
                    healAmount = healthMissing
                self.health += healAmount
                print(f"You took a moment to rest.")
                time.sleep(1)
                print(f"You recovered {healAmount} health.")
                time.sleep(1)
                if self.health == self.maxHealth:
                    print("You are at max health.")
                elif self.health > self.maxHealth*0.75:
                    print("You are at more than 75\u0025 health.")
                elif self.health == self.maxHealth*0.75:
                    print("You are at 75\u0025 health.")
                elif self.health < self.maxHealth*0.75:
                    print("You are at less than 50\u0025 health.")
                elif self.health > self.maxHealth*0.5:
                    print("You are at more than 50\u0025 health.")
                elif self.health == self.maxHealth*0.5:
                    print("You are at 50\u0025 health.")
                elif self.health < self.maxHealth*0.5:
                    print("You are at less than 75\u0025 health.")
                elif self.health > self.maxHealth*0.25:
                    print("You are at more than 25\u0025 health.")
                elif self.health == self.maxHealth*0.25:
                    print("You are at 25\u0025 health.")
                elif self.health < self.maxHealth*0.25:
                    print("You are at less than 25\u0025 health.")
                time.sleep(1)
            else:
                print("You are at max health.")
                time.sleep(1)
        #     self.findDead(main.getDead (floor, room)) 
            
        while len(enemies) > 0 and player.health > 0:
            for enemy in enemies:
                enemy.turn()
                time.sleep(1)
            time.sleep(1)    
            player.turn()
            time.sleep(1)
        if room < 9:
            self.enterRoom(floor, room + 1)
        elif floor < 9:
            self.enterRoom(floor + 1, 1)
        else:
            self.enterRoom(floor, room + 1)

    def findDead(self, dead):
        char=" "
        index=0
        choosing = True
        deadItems = []
        for item in dead:
            if agedItem[item] != None:
                deadItems.append(item)
        # print(f"You come across th body of a fallen {dead[0]} and decide to search it...")
        print(f"You come across a dead body and decide to search it...")
        while char!=10 and choosing:
            char=window.getch()
            # print("pressed", char)
            print("Choose an item to take:\n")
            ## add logif fow was/awwors
            if char == ord("a"):
                index -= 1
            elif char == ord("d"):
                index += 1
            index %= len(deadItems)

            
            window.clear()
            
            for i,card in enumerate(deadItems):
                if i == index:
                    color = "\x1b[44m"
                else:
                    color = "\x1b[0m"
                print(color, card,end="\x1b[0m, ", sep="")
            print("\x1b[0m\n", itemDescriptions[deadItems[index]])
            time.sleep(0.1)
        choosing = False
        card = self.hand[index]
        
    def updateDescriptions(self):
        self.cardDescriptions = {
            "Attack" : f"Deal {self.damageMod} damage to target enemy",
            "Defend" : f"Block {self.defenseMod} damage on the enemy's next turn",
            "Warrior's Strike" : f"Deal {self.damageMod+1} damage to target enemy",
            "Warrior's Defense" : f"Block {self.defenseMod+1} damage on the enemy's next turn",
            "Shield Bash" : f"Deal damage {self.damageMod//2} to target enemy and block {self.defenseMod//2 + 1} damage on the enemy's next turn",
            "Sword Slash" : f"Deal {self.damageMod//2 +1} damage to ALL enemies",
            "Cunning Strike": f"Deal {self.damageMod+1} damage to target enemy",
            "Desperate Dodge": "Dodge the next three attacks",
            "Enhanced Relexes": f"Increase the chance that you dodge an attack automatically by 25\u0025 (new chance:{self.dodgeChance}), resets every room",
            "Counterstrike": "Attack the next enemy that attacks you (even if they miss)",
            "Dodge": "Dodge the next attack"
        }

    def turn(self):
        self.damageMod = 1
        self.defenseMod = 1
        self.defense = 0
        for item in self.items:
            itemAbility = itemAbilities[item]
            exec(itemAbility)
        


        for i in range(self.handSize):
            if self.deck == []:
                self.deck = self.discard
                self.discard = []
            card = random.choice(self.deck)
            self.hand.append(card)
            self.deck.remove(card)
        
        self.playCard()
        time.sleep(1)
        if self.archetype == "Slink" and len(enemies) > 0:
            self.playCard()
        for card in self.hand:
            self.discard.append(card)
        self.hand = []

    def playCard(self):
        char=" "
        index=0
        choosing = True
        while char!=10 and choosing:
            char=window.getch()
            # print("pressed", char)
            # display(Image(filename='OpenGameArt_Slime_Madjestiko.png'))
            info = f"you({self.health} hp),   "
            for enemy in enemies:
                info += f"{enemy.name}({enemy.health} hp, {enemy.defense} defense),   "
            # print(info)
            print("\nChoose a card:\n")
            ## add logif fow was/awwors
            if char == ord("a"):
                index -= 1
            elif char == ord("d"):
                index += 1
            index %= len(self.hand)

            
            window.clear()
            
            for i,card in enumerate(self.hand):
                if i == index:
                    color = "\x1b[44m"
                else:
                    color = "\x1b[0m"
                print(color, card,end="\x1b[0m, ", sep="")
            self.updateDescriptions()
            print("\x1b[0m\n", self.cardDescriptions[self.hand[index]])
            time.sleep(0.1)
        choosing = False
        card = self.hand[index]
        self.hand.remove(card)
        self.discard.append(card)   
        action=actions[card]
        char=" "
        index=0
        choosing = True
        if card in cardsWithTargets:
            while char!=10 and choosing:
                char=window.getch()
                # print("pressed", char)
                print("Choose a target:\n")
                ## add logif fow was/awwors
                if char == ord("a"):
                    index -= 1
                elif char == ord("d"):
                    index += 1
                index %= len(enemies)

                
                window.clear()
                
                for i,enemy in enumerate(enemies):
                    if i == index:
                        color = "\x1b[44m"
                    else:
                        color = "\x1b[0m"
                    print(color, enemy.sprite,end="\x1b[0m   ", sep="")
                info = f"{enemy.name}({enemies[index].health} hp, {enemies[index].defense} defense)"
                # if enemy.splitting:
                #     info = info + ", splitting"
                print("\x1b[0m\n", info)
                time.sleep(0.1)
            choosing = False
            target = enemies[index]
        print(f'You used "{card}"!')
        time.sleep(1)
        exec(action)
        if card == "Shield Bash":
            self.defense += self.defenseMod//2 + 1
       



class Enemy():
    def __init__(self, name = "enemy", maxHealth = 0, justSplit = False):
        self.floor = 1
        self.room = 1
        self.items = []
        self.items = []
        self.deck = ["Attack", "Attack", "Attack"]
        self.discard = []
        self.maxHealth = maxHealth
        self.defense = 0
        self.handSize = 3
        self.damageMod = 3
        self.defenseMod = 3
        self.splitting = False
        self.justSplit = justSplit
        self.name = name
        self.sprite = "\ufffd"
        if self.name == "slime":
            if self.maxHealth == 0:
                self.maxHealth = random.randrange(15, 30  + 5*(player.floor-1))
            self.deck.append("Ooze")
            self.deck.append("Split")
            color = random.choice(slimeColors)
            self.sprite = color + random.choice(slimeSprites) + "\033[0m"
        elif self.name == "Dungeon Lizard":
            self.maxHealth = random.randrange(3, 10  + 1*(player.floor-1))
            color = random.choice(lizardColors)
            self.sprite = color + "\U0001318C    " + "\033[0m"
            self.damageMod = random.randrange(1, 3)
        else:
            self.maxHealth = random.randrange(10, 25 + 5*(player.floor-1))
            self.deck.append("Defend")
            self.deck.append("Defend")
            # self.sprite = random.choice(enemySprites)
            self.items.append(random.choice(weapons))
            for i in range(random.randrange(0, 2)):
                self.items.append(random.choice(nonWeaponItems))
            

        self.health = self.maxHealth

    def  die(self):
        time.sleep(1)
        print(f'The {self.name} was defeated!')
        for item in self.items:
            aged = agedItem[item]
            if aged != None:
                print(f"You got the {self.name}'s {aged}! ({itemDescriptions[aged]})")
                player.items.append(aged)
                time.sleep(1)
        enemies.remove(self)

    def takeDamage(self, amount):
        damageTaken = amount - self.defense
        if damageTaken < 0:
            damageTaken = 0
        damageBlocked = amount - damageTaken
        if self.defense > 0:
            message = f"blocked {damageBlocked} damage and"
        else:
            message = ""
        
        self.health -= damageTaken
        time.sleep(1)
        print(f'The {self.name} {message} took {damageTaken} damage')
        if self.health <= 0:
            if 1 <= self.floor <= 9:
                self.die()
        elif "Split" in self.deck and self.health < 4:
            self.splitting = False
            self.deck.remove("Split")
            time.sleep(1)
            print("The slime is too weak to split!")

    def turn(self):
        self.defense = 0
        for item in self.items:
            itemAbility = itemAbilities[item]
            exec(itemAbility)
        if self.health <= 0:
            if 1 <= self.floor <= 9:
                self.die()
        if self.justSplit:
            self.justSplit = False
        elif self.splitting:
            if self.health >= 4:
                self.health//=2
                enemies.append(Enemy("slime", self.health, True))
                time.sleep(1)
                print("The slime split in two!")
            else:
                time.sleep(1)
                print("The slime is too weak to split!")
            self.splitting = False
        else:
            if self.deck == []:
                self.deck = self.discard
                self.discard = []
            card=random.choice(self.deck)
            ## remove card from posible choices
            action=actions[card]
            target = player
            time.sleep(1)
            print(f'The {self.name} used "{card}"!')
            exec(action) # exec or eval could work
            self.deck.remove(card)
            self.discard.append(card)


if __name__ =="__main__":

    player = Player("Slink")
    enemies = []
    # enemies.append(Enemy())
    # enemies.append(Enemy("slime"))

    def attackPlayer(damage:int):
        player.takeDamage(damage)
    player.enterRoom(1, 1)
    
    
    
