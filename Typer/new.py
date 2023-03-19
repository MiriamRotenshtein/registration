import typer
import json
from typing import List

app = typer.Typer()

# readTheFile
@app.command()
def readJson():
    with open('json.json', 'r',encoding='utf-8') as f:
        arr=f.readlines()
    return arr


user=[]

class User():
    def __init__(self, fn, ln):
        self.fn=fn
        self.ln=ln

@app.command()
def changeToDict(myList):
    userDict={'fn':myList.fn,'ln':myList.ln}
    return userDict    

#add json
@app.command()
def add():
    print(type(readJson()))   
    firstName=input('enter firstName:')
    lastName=input('enter lastName:')
    name=User(firstName,lastName)
    user.append(name)    
    with open('json.json', 'a') as f:
         json.dump([changeToDict(u) for u in user], f)    
   
#read last 10
@app.command()
def readTen():
    arr=readJson()
    print(arr[0])
    return arr[len(arr):len(arr)-10:-1]

# function activation
print("add()")
add()
print("readTen()")
print(readTen())


