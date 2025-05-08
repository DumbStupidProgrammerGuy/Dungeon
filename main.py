from fastapi import FastAPI
app = FastAPI()
import random

deads = []
for floor in range(9):
    deads.append([ set() for room in range(9)])


@app.get("/hi")
def hi ():
    return "hi"



@app.put("/dead")
def dies (floor:int, room:int, items:str):
    itemsList=items.split(",")
    print(itemsList)
    deads[floor][room].update(itemsList)


@app.put("/getDead")
def getDead (floor:int, room:int):
    return deads[floor][room]
