from fastapi import FastAPI
app = FastAPI()
import random

deads = []
for floor in range(9):
    deads.append([ set() for room in range(9)])

champs = []

@app.get("/hi")
def hi ():
    return "hi"

@app.put("/dead")
def die (floor:int, room:int, items:str):
    itemsList=items.split(",")
    deads[floor][room].update(itemsList)

@app.get("/getDead")
def getDead (floor:int, room:int):
    return deads[floor][room]

@app.put("/putChamp")
def putChamp (room:int, deck:str, items:str):
    deckList=deck.split(",")
    itemsList=items.split(",")
    champs.insert(room-1, [deckList, itemsList])

@app.get("/getChamp")
def getChamp (rank:int):
    return champs[rank]


# uvicorn main:app --host 0.0.0.0 --port 8096

class Player():
    def __init__(self):
        self.floor = 1
        self.room = 1
        self.items = ""
        self.deck = "attack, defend"
        self.health = 100
        self.defense = 0

    def takeDamage(self, amount:int):
        self.health -= amount - self.defense
        if self.health <= 0:
            if self.floor == 10:
                putChamp(self.room, self.deck, self.items)
            elif 1 <= self.floor <= 9:
                die(self.floor, self.room, self.items)

player = Player()

@app.put("/attackPlayer")
def attackPlayer(damage:int):
    player.takeDamage(damage)