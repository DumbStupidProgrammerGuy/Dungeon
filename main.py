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
def dies (floor:int, room:int, items:str):
    itemsList=items.split(",")
    print(itemsList)
    deads[floor][room].update(itemsList)

@app.put("/champ")
def champDies (room:int, deck:str, items:str):
    itemsList=items.split(",")
    print(itemsList)
    champs.insert(room-1, [deck, itemsList])

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
        self.items = []
        self.deck = []
        self.health = 100