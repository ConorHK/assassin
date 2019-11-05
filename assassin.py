from random import shuffle

def loadPlayers():
    players = []

    with open("Lists/players.txt") as file:
            players = file.read().splitlines()

    playersUpper = list(map(str.upper, players))
    return playersUpper

def loadWeapons():
    weapons = []

    with open("Lists/weapons.txt") as file:
            weapons = file.read().splitlines()

    weaponsUpper = list(map(str.upper, weapons))
    return weaponsUpper

def loadRestrictions():
    restrictions = []

    with open("Lists/restrictions.txt") as file:
        restrictions = file.read().splitlines()

    restrictionsUpper = list(map(str.upper, restrictions))
    return restrictionsUpper

def main():
    players = loadPlayers()
    shuffle(players)

    weapons = loadWeapons()
    shuffle(weapons)

    restrictions = loadRestrictions()
    shuffle(restrictions)

    targets = players[:]
    targetOutput = [] # array for output to targetlist file for eliminate.py
    total = len(players)

    lines = []

    for i in range(total):
        lines.append(players[i] + "  >>> Target: " + targets[(i+1) % total] +  "  >>> Weapon: " +  weapons[i]  + "  >>> Restriction: " + restrictions[i] + "\n\n")
        targetOutput.append(targets[(i+1) % total])
    with open("TempGameFiles/targetlist.txt", "w") as file:
        for item in targetOutput:
            file.write("%s\n" % item)
    with open("TempGameFiles/playershuffle.txt", "w") as file:
        for item in players:
            file.write("%s\n" % item)
    with open("TempGameFiles/weaponshuffle.txt", "w") as file:
        for item in weapons:
            file.write("%s\n" % item)
    with open("TempGameFiles/restrictionshuffle.txt", "w") as file:
        for item in restrictions:
            file.write("%s\n" % item)
    with open("targets.txt", "w") as file:
        line = sorted(lines, key=str.lower )
        for line in lines:
            file.write(line)

main()
