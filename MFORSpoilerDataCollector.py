import json, sys, os, copy

blankDict ={
    "Morph Ball":0,
    "Super Missile Data":0,
    "Hi-Jump Boots":0,
    "Space Jump":0,
    "Bombs":0,
    "Power Bomb Data":0,
    "Gravity Suit":0,
    "Diffusion Data":0,
    "Wave Beam":0,
    "Ice Missile Data":0,
    "Charge Beam":0,
    "Missile Data":0,
    "Ice Beam":0,
    "Varia Suit":0,
    "Plasma Beam":0,
    "Wide Beam":0,
    "Speed Booster":0,
    "Screw Attack":0,
    "Energy Tank":0,
    "Missile Tank":0,
    "Power Bomb Tank":0}

bossDict = {
    "Arachnus":copy.copy(blankDict),
    "Yakuza":copy.copy(blankDict),
    "Charge Core-X":copy.copy(blankDict),
    "Ridley":copy.copy(blankDict),
    "Zazabi":copy.copy(blankDict),
    "Nettori":copy.copy(blankDict),
    "Wide Core-X":copy.copy(blankDict),
    "Serris":copy.copy(blankDict),
    "Nightmare":copy.copy(blankDict),
    "Mega Core-X":copy.copy(blankDict),
    "Box-2":copy.copy(blankDict),
    "Data S0":copy.copy(blankDict),
    "Data S2":copy.copy(blankDict),
    "Data S3":copy.copy(blankDict),
    "Data S4":copy.copy(blankDict),
    "Data S5":copy.copy(blankDict)}

def main():
    spoilerDirectory = "C:\\YOUR\\MFOR\\SPOILERLOG\\FOLDER\\HERE\\"
    
    global bossDict
    
    for filename in os.listdir(spoilerDirectory):
        for boss in bossDict:
            getInfo(json.load(open(spoilerDirectory + filename)), boss, bossDict[boss])

    for dicti in bossDict:
        print("\n" + dicti + ":")
        for item in bossDict[dicti]:
            print(item + " : " + str(bossDict[dicti][item]) + ", " + str(round(bossDict[dicti][item], 2)) + "%")
    

def getInfo(logData, bossName, bossDict):
    
    if logData["Items"][bossName] == "Morph Ball":
        bossDict["Morph Ball"] = bossDict["Morph Ball"] + 1
        
    if logData["Items"][bossName] == "Super Missile Data":
        bossDict["Super Missile Data"] = bossDict["Super Missile Data"] + 1
        
    if logData["Items"][bossName] == "Hi-Jump Boots":
        bossDict["Hi-Jump Boots"] = bossDict["Hi-Jump Boots"] + 1
        
    if logData["Items"][bossName] == "Space Jump":
        bossDict["Space Jump"] = bossDict["Space Jump"] + 1
        
    if logData["Items"][bossName] == "Bombs":
        bossDict["Bombs"] = bossDict["Bombs"] + 1
        
    if logData["Items"][bossName] == "Power Bomb Data":
        bossDict["Power Bomb Data"] = bossDict["Power Bomb Data"] + 1
        
    if logData["Items"][bossName] == "Gravity Suit":
        bossDict["Gravity Suit"] = bossDict["Gravity Suit"] + 1
        
    if logData["Items"][bossName] == "Diffusion Data":
        bossDict["Diffusion Data"] = bossDict["Diffusion Data"] + 1
        
    if logData["Items"][bossName] == "Wave Beam":
        bossDict["Wave Beam"] = bossDict["Wave Beam"] + 1
        
    if logData["Items"][bossName] == "Ice Missile Data":
        bossDict["Ice Missile Data"] = bossDict["Ice Missile Data"] + 1
        
    if logData["Items"][bossName] == "Charge Beam":
        bossDict["Charge Beam"] = bossDict["Charge Beam"] + 1
        
    if logData["Items"][bossName] == "Missile Data":
        bossDict["Missile Data"] = bossDict["Missile Data"] + 1
        
    if logData["Items"][bossName] == "Ice Beam":
        bossDict["Ice Beam"] = bossDict["Ice Beam"] + 1
        
    if logData["Items"][bossName] == "Varia Suit":
        bossDict["Varia Suit"] = bossDict["Varia Suit"] + 1
        
    if logData["Items"][bossName] == "Plasma Beam":
        bossDict["Plasma Beam"] = bossDict["Plasma Beam"] + 1
        
    if logData["Items"][bossName] == "Wide Beam":
        bossDict["Wide Beam"] = bossDict["Wide Beam"] + 1
        
    if logData["Items"][bossName] == "Speed Booster":
        bossDict["Speed Booster"] = bossDict["Speed Booster"] + 1
        
    if logData["Items"][bossName] == "Screw Attack":
        bossDict["Screw Attack"] = bossDict["Screw Attack"] + 1
        
    if logData["Items"][bossName] == "Energy Tank":
        bossDict["Energy Tank"] = bossDict["Energy Tank"] + 1
        
    if logData["Items"][bossName] == "Missile Tank":
        bossDict["Missile Tank"] = bossDict["Missile Tank"] + 1
        
    if logData["Items"][bossName] == "Power Bomb Tank":
        bossDict["Power Bomb Tank"] = bossDict["Power Bomb Tank"] + 1
    
if __name__ == "__main__":
    main()
