import main # replace with api filename



class Player():
    def __init__(self):
        self.floor = 1
        self.room = 1
        self.items = ""
        self.deck = "attack, defend"
        self.health = 100
        self.defense = 0

    def putChamp(room,deck,items):
        main.putChamp(room,deck,items)
    
    def  die(floor, room, items):
        main.putDead(self.floor, self.room, self.items)

    def takeDamage(self, amount):
        self.health -= amount - self.defense
        
        if self.health <= 0:
            if self.floor == 10:
                self.putChamp(self.room, self.deck, self.items)
            elif 1 <= self.floor <= 9:
                self.die(self.floor, self.room, self.items)



if __name__ =="__main__":

    player = Player()

    def attackPlayer(damage:int):
        player.takeDamage(damage)
    attackPlayer(2)
    

