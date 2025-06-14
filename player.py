import main # replace with api filename
import random
import getch
import curses
import time
window = curses.initscr()
window.nodelay(True)
curses.noecho()

actions={
    "Attack":"target.takeDamage(3)",
    "Defend":"self.defense += 3"
}

descriptions = {
    "Attack" : "Deal 3 damage to target enemy",
    "Defend" : "Block 3 damage on the enemy's next turn"
}

class Player():
    def __init__(self, archetype = None):
        self.archetype = archetype
        self.floor = 1
        self.room = 1
        self.items = []
        self.deck = ["Attack", "Attack", "Attack"]
        self.maxHealth = 100
        self.defense = 0
        self.handSize = 3
        self.damageMod = 3
        self.defenseMod = 3
        self.hand = []
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
        main.putDead(self.floor, self.room, ", ".join(self.items))

    def takeDamage(self, amount):
        self.health -= amount - self.defense
        
        if self.health <= 0:
            if self.floor == 10:
                self.putChamp()
            elif 1 <= self.floor <= 9:
                self.die()

    def enterRoom(self, floor, room):
        self.floor = floor
        self.room = room


    def turn(self):
        self.damageMod = 3
        self.defenseMod = 3
        if "Warrior's Sword" in self.items:
            self.damageMod += 1
        if "Warrior's Sheild" in self.items:
            self.defenseMod += 1

        for i in range(self.handSize):
            self.hand.append(random.choice(self.deck))
        print("Choose a card:\n",self.hand)
        char=" "
        index=0
        while char!="\n":
            char=window.getch()
            print("pressed", char)
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
            print("\x1b[0m\n", descriptions[self.hand[index]])
            time.sleep(0.1)


class Enemy():
    def __init__(self, name = "enemy"):
        self.floor = 1
        self.room = 1
        self.items = []
        self.deck = ["Attack", "Attack", "Attack"]
        self.maxHealth = 100
        self.defense = 0
        self.handSize = 3
        self.defendAmount = 3
        self.name = name
        if self.name == "slime":
            self.maxHealth = random.randrange(30, 70)
            self.deck.append("Ooze")
            self.deck.append("Split")
        else:
            self.maxHealth = random.randrange(30, 70)
            self.deck.append("Defend")
            self.deck.append("Defend")
            self.deck.append("Defend")

    def  die(self):
        pass

    def takeDamage(self, amount):
        self.health -= amount - self.defense
        
        if self.health <= 0:
            if 1 <= self.floor <= 9:
                self.die()

    def turn(self):
        card=random.choice(self.deck)
        ## remove card from posible choices
        action=actions[card]
        target = player
        exec(action) # exec or eval could work
        print(f'The {self.name} used "{card}"!')
        # hi


if __name__ =="__main__":

    player = Player()
    enemy = Enemy()

    def attackPlayer(damage:int):
        player.takeDamage(damage)
    enemy.turn()
    print()
    
