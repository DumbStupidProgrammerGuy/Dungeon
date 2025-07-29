import main # replace with api filename
import random
import getch
import curses
import time
window = curses.initscr()
window.nodelay(True)
curses.noecho()

enemyTypes=["enemy", "slime"]

actions={
    "Attack":"target.takeDamage(self.damageMod)",
    "Defend":"self.defense += self.defenseMod",
    "Warrior's Strike":"target.takeDamage(self.damageMod+1)",
    "Warrior's Defense":"self.defense += self.defenseMod+1",
    "Shield Bash" : "target.takeDamage(self.damageMod//2)",
    "Sword Slash":"for enemy in enemies: enemy.takeDamage(self.damageMod//2)",
    "Split":'self.splitting = True',
    "Ooze": "target.takeDamage(target.defense + self.health//10)"
}

cardsWithTargets=[
    "Attack",
    "Warrior's Strike",
    "Shield Bash"]


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
        self.damageMod = 3
        self.defenseMod = 3
        self.hand = []
        self.descriptions = {
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
            self.deck.append("Counterstrike")
            self.items.append("Slink's Daggers")
            self.items.append("Slink's Hood")
            self.deck.append("Dodge")
            self.deck.append("Dodge")
            self.deck.append("Dodge")
            self.handSize = 5
            self.maxHealth = 80
            self.dodges = 0
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

    def takeDamage(self, amount):
        self.health -= amount - self.defense
        if self.defense > 0:
            message = f"blocked {self.defense} damage and"
        else:
            message = ""
        damageTaken = amount - self.defense
        if damageTaken < 0:
            damageTaken = 0
        time.sleep(1)
        print(f'You {message} took {damageTaken} damage')
        time.sleep(1)
        if self.health <= 0:
            if self.floor == 10:
                self.putChamp()
            elif 1 <= self.floor <= 9:
                self.die()

    def enterRoom(self, floor, room):
        print(f"Entering floor {floor}, room {room}...")
        time.sleep(5)
        self.floor = floor
        self.room = room
        r = random.randrange(0, 3)
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
        

    def updateDescriptions(self):
        self.descriptions = {
            "Attack" : f"Deal {self.damageMod} damage to target enemy",
            "Defend" : f"Block {self.defenseMod} damage on the enemy's next turn",
            "Warrior's Strike" : f"Deal {self.damageMod+1} damage to target enemy",
            "Warrior's Defense" : f"Block {self.defenseMod+1} damage on the enemy's next turn",
            "Shield Bash" : f"Deal damage {self.damageMod//2} to target enemy and block {self.defenseMod-1} damage on the enemy's next turn",
            "Sword Slash" : f"Deal {self.damageMod//2} damage to ALL enemies"
        }

    def turn(self):
        self.damageMod = 3
        self.defenseMod = 3
        self.defense = 0
        if "Warrior's Sword" in self.items:
            self.damageMod += 1
        if "Warrior's Sheild" in self.items:
            self.defenseMod += 2
            # self.defense = 2

        for i in range(self.handSize):
            if self.deck == []:
                self.deck = self.discard
                self.discard = []
            card = random.choice(self.deck)
            self.hand.append(card)
            self.deck.remove(card)
        
        char=" "
        index=0
        choosing = True
        while char!=10 and choosing:
            char=window.getch()
            # print("pressed", char)
            print("Choose a card:\n")
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
            print("\x1b[0m\n", self.descriptions[self.hand[index]])
            time.sleep(0.1)
        window.clear()
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
                    print(color, enemy.name,end="\x1b[0m, ", sep="")
                info = f"{enemies[index].health} health, {enemies[index].defense} defense"
                # if enemy.splitting:
                #     info = info + ", splitting"
                print("\x1b[0m\n", info)
                time.sleep(0.1)
            window.clear()
            choosing = False
            target = enemies[index]
        print(f'You used "{card}"!')
        time.sleep(1)
        exec(action)
        if card == "Shield Bash":
            self.defense += self.defenseMod-1
        for card in self.hand:
            self.discard.append(card)
        self.hand = []
       



class Enemy():
    def __init__(self, name = "enemy", maxHealth = 0):
        self.floor = 1
        self.room = 1
        self.items = []
        self.deck = ["Attack", "Attack", "Attack"]
        self.discard = []
        self.maxHealth = maxHealth
        self.defense = 0
        self.handSize = 3
        self.damageMod = 3
        self.defenseMod = 3
        self.splitting = False
        self.name = name
        if self.name == "slime":
            if self.maxHealth == 0:
                self.maxHealth = random.randrange(15, 30  + 5*(player.floor-1))
            self.deck.append("Ooze")
            self.deck.append("Split")
        else:
            self.maxHealth = random.randrange(10, 25 + 5*(player.floor-1))
            self.deck.append("Defend")
            self.deck.append("Defend")
        self.health = self.maxHealth

    def  die(self):
        time.sleep(1)
        print(f'The {self.name} was defeated!')
        enemies.remove(self)

    def takeDamage(self, amount):
        self.health -= amount - self.defense
        if self.defense > 0:
            message = f"blocked {self.defense} damage and"
        else:
            message = ""
        
        damageTaken = amount - self.defense
        if damageTaken < 0:
            damageTaken = 0
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
        if self.health <= 0:
            if 1 <= self.floor <= 9:
                self.die()
        if self.splitting:
            if self.health >= 4:
                self.health//=2
                enemies.append(Enemy("slime", self.health))
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

    player = Player("Warrior")
    enemies = []
    # enemies.append(Enemy())
    # enemies.append(Enemy("slime"))

    def attackPlayer(damage:int):
        player.takeDamage(damage)
    player.enterRoom(1, 1)
    
    
    
