from fastapi import FastAPI # install with pip install fastapi uvicorn
app = FastAPI()
import random


deads = []
for floor in range(9):
    deads.append([ set() for room in range(9)])

champs = []

@app.get("/hi")
def hi ():
    return "hi"

@app.put("/putDead")
def putDead (floor:int, room:int, archetype:str, deck:str, items:str):
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


