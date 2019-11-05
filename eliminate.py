import sys

# Function that loads in the players in the current play order.
def loadPlayers():
    players = []

    with open("TempGameFiles/playershuffle.txt") as file:
        players = file.read().splitlines()
    
    return players
def loadTargets():
    targets = []

    with open("TempGameFiles/targetlist.txt") as file:
        targets = file.read().splitlines()

    return targets
def loadWeapons():
    weapons = [] 

    with open("TempGameFiles/weaponshuffle.txt") as file:
        weapons = file.read().splitlines()

    return weapons
def loadRestrictions():
    restrictions = []

    with open("TempGameFiles/restrictionshuffle.txt") as file:
        restrictions = file.read().splitlines()

    return restrictions

# Functions that update the lists for current play order.
def loadCurrentPlayers(count, list):
    players = []
    with open("TempGameFiles/playershuffle.txt") as file:
        players = file.read().splitlines()
    return players

def loadCurrentWeapons(count, list):
    weapons = []
    with open("TempGameFiles/weaponshuffle.txt") as file:
        weapons = file.read().splitlines()


    return weapons

def loadCurrentRestrictions(count, list):
    restrictions = []

    with open("TempGameFiles/restrictionshuffle.txt") as file:
        restrictions = file.read().splitlines()

    return restrictions

def loadCurrentTargets(count, list):
    targets = []
    with open("TempGameFiles/targetlist.txt") as file:
        targets = file.read().splitlines()

    return targets


# Linked list implementation:
# Followed guide written by Usman Malik @stackabuse.com
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None  # pointer points to nothing initially.


class LinkedList:
    #Initializes list
    def __init__(self):
        self.start_node = None

    #Travels through list and updates current play files accordingly
    def traverse_list(self, path):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            open("TempGameFiles/%s" % path, "w").close() 

            while n is not None:
                #print(n.item, " ")
                with open("TempGameFiles/%s" % path, "a") as file:
                    file.write(n.item + "\n")
                n = n.ref

    #Insert functions
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node;
    
    # Function that returns how many elements are in the list
    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    # Function that checks if an element is in the list
    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                return True
            n = n.ref
        print("Item not found")
        return False
   
   # Function that returns item at index
    def return_item(self, index):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        if index == 1:
            return self.start_node.item
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("Index is out of bounds.")
        else:
            return n.ref.item

    # Delete functions
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete.")
            return

        #Delete first node:
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return 1

        n = self.start_node
        i = 2; #to account for 1 offset
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
            i = i + 1

        if n.ref is None:
            print("Item not found in list test")
        else:
            n.ref = n.ref.ref
            return i

    def delete_element_by_index(self, index):
        if self.start_node is None:
            print("The list has no elements to delete.")
        
        # Delete first node:
        if index == 1:
            self.start_node = self.start_node.ref
            return
        
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("Index out of bounds.")
        else:
            n.ref = n.ref.ref

def main():
    # Initializing lists:
    players = loadPlayers()
    weapons = loadWeapons()
    restrictions = loadRestrictions()
    targets = loadTargets()
    lines = []
    
    # Initialize list and populate with players.
    player_list = LinkedList()
    for item in players:
        player_list.insert_at_end(item)
    weapon_list = LinkedList()
    for item in weapons:
        weapon_list.insert_at_end(item)
    restriction_list = LinkedList()
    for item in restrictions:
        restriction_list.insert_at_end(item)
    target_list = LinkedList()
    for item in targets:
        target_list.insert_at_end(item)

    #Bool for seeing if input is valid
    flag = player_list.search_item(str(sys.argv[1]))
    if(flag):
        # if so, delete the eliminated player and the corresponding weapon and restriction
        player_list.delete_element_by_value(str(sys.argv[1]))
        index = target_list.delete_element_by_value(str(sys.argv[1]))
        weapon_list.delete_element_by_index(index)
        restriction_list.delete_element_by_index(index)

        # run traverse list to update current play files to ensure persistance
        player_list.traverse_list("playershuffle.txt")
        target_list.traverse_list("targetlist.txt")
        weapon_list.traverse_list("weaponshuffle.txt")
        restriction_list.traverse_list("restrictionshuffle.txt")

        # Re-initialize lists
        players = loadCurrentPlayers(player_list.get_count(), player_list)
        targets = loadCurrentTargets(target_list.get_count(), target_list)
        weapons = loadCurrentWeapons(weapon_list.get_count(), weapon_list)
        restrictions = loadCurrentRestrictions(restriction_list.get_count(), restriction_list)

        # Print to file
        for i in range(len(players)):
            lines.append(players[i] + "  >>> Target: " + targets[i] +  "  >>> Weapon: " + weapons[i]  + "  >>> Restriction: " + restrictions[i] + "\n\n") 
        
        with open("current.txt", "w") as file:
            for line in lines:
                file.write(line)
main()
