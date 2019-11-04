from random import shuffle

def loadPlayers():
    players = []

    with open("players.txt") as file:
            players = file.read().splitlines()

    playersUpper = list(map(str.upper, players))
    return playersUpper

def loadWeapons():
    weapons = []

    with open("weapons.txt") as file:
            weapons = file.read().splitlines()

    weaponsUpper = list(map(str.upper, weapons))
    return weaponsUpper

def loadRestrictions():
    restrictions = []

    with open("restrictions.txt") as file:
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
    total = len(players)

    lines = []

    for i in range(total):
        lines.append(players[i] + "  >>> Target: " + targets[(i+1) % total] +  "  >>> Weapon: " +  weapons[i]  + "  >>> Restriction: " + restrictions[i] + "\n\n")

    with open("targets.txt", "w") as file:
        file.write("\n---------------------------------------------TARGET LIST-------------------------------------\n\n")
        line = sorted(lines, key=str.lower )
        for line in lines:
            file.write(line)
        file.write("----------------------------------------------------------------------------------------------")

main()
