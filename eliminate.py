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

def loadCurrentPlayers(count, list):
    players = []

    for i in range(count):
            players.append(list.return_item(i))

    return players

def loadCurrentWeapons(count, list):
    weapons = []

    for i in range(count):
            weapons.append(list.return_item(i))

    return weapons

def loadCurrentRestrictions(count, list):
    restrictions = []

    for i in range(count):
            restrictions.append(list.return_item(i))

    return restrictions


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

    #Travels through list and prints elements
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    #Insert functions
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node;

    def insert_after_item(self, x, data):

        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("ERROR: Item not in list.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no elements.")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bounds.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
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
    # Function for user input creation of lists
    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node: "))
            self.insert_at_end(value)
    
    # Delete element functions
    def delete_at_start(self):
        if self.start_node is None:
            print("This list has no elements to delete.")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no elements to delete.")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete.")
            return

        #Delete first node:
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        i = 2; #to account for 1 offset
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
            i = i + 1

        if n.ref is None:
            print("Item not found in list")
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
    
    flag = player_list.search_item(str(sys.argv[1]))
    if(flag):
        player_list.traverse_list()
        print("\n")
        weapon_list.traverse_list()
        print("\n")
        restriction_list.traverse_list()
        print("\n")
        index = player_list.delete_element_by_value(str(sys.argv[1]))
        weapon_list.delete_element_by_index(index)
        restriction_list.delete_element_by_index(index)
        player_list.traverse_list()
        print("\n")
        weapon_list.traverse_list()
        print("\n")
        restriction_list.traverse_list()
        print("\n")
        
        players = loadCurrentPlayers(player_list.get_count(), player_list)
        weapons = loadCurrentWeapons(weapon_list.get_count(), weapon_list)
        restrictions = loadCurrentRestrictions(restriction_list.get_count(), restriction_list)

        for i in range(player_list.get_count()):
            lines.append(players[i] + "  >>> Target: " + targets[i] +  "  >>> Weapon: " + weapons[i]  + "  >>> Restriction: " + restrictions[i] + "\n\n") 
        
        with open("current.txt", "w") as file:
            line = sorted(lines, key=str.lower)
            for line in lines:
                file.write(line)
main()
