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
def die (floor:int, room:int, deck:str, items:str):
    deckList=deck.split(",")
    itemsList=items.split(",")
    if floor == 10:
        champs.insert(room-1, [deckList, itemsList])
    else:
        deads[floor][room].update(itemsList)

@app.put("/getDead")
def getDead (floor:int, room:int):
    return deads[floor][room]

@app.put("/getChamp")
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
            die(self.floor, self.room, self.deck, self.items)

player = Player()

@app.put("/attackPlayer")
def attackPlayer(damage:int):
    player.takeDamage(damage)