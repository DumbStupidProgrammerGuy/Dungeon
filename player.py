import main # replace with api filename
import random
actions={
    "Attack":"self.attack()",
    "Defend":"self.defense += 3"
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

    def turn(self):
        for i in range(self.handSize):
            self.hand.append(random.choice(self.deck))



if __name__ =="__main__":

    player = Player("Slink")

    def attackPlayer(damage:int):
        player.takeDamage(damage)
    attackPlayer(2)
    
class enemy():
    def __init__(self, type = None):
        self.floor = 1
        self.room = 1
        self.items = []
        self.deck = ["Attack", "Attack", "Attack"]
        self.maxHealth = 100
        self.defense = 0
        self.handSize = 3
        self.defendAmount = 3
        if type == "slime":
            self.maxHealth = random.randrange(30, 70)
            self.deck.append("Ooze")
            self.deck.append("Split")
        else:
            self.maxHealth = random.randrange(30, 70)
            self.deck.append("Defend")
            self.deck.append("Defend")
            self.deck.append("Defend")

    def turn(self):
        card=random.choice(self.deck)
        ## remove card from posible choices
        action=actions[card]
        exec(action) # exec or eval could work