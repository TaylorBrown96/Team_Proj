#Room Class

from Container import Container
from Item import Item

class Room(Container):
    """class for holding room names descriptions, exits"""       
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.door = None
        self.chest = None
        self.lockedexit = None
        self.contents = {} # First pass at items in rooms 
        #dictionary for containers
        
    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = self.name + "\n"
        text += self.description + "\n"
        # append all exits
        exitList = self.exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self.exits[direction]  # prints in format "North: Living Room", etc.
            text += "\n"
        # print items in room, if any
        if self.contents == {}:
            text += "There's no items here.\n"
        else:
            text += "In this room you see: \n"
            text += self.listContents()
            # for item in self.contents:
            #     text += item.name + ": " + item.description + "\n"
        # display door in room, if any
        if self.door != None:
            text += "There is a door here to the: " + self.lockedexit + "\n"
            text += self.door.name + "\n"
            text += self.door.description + "\n"
        # display chest in room, if any
        if self.chest != None:
            text += "There is a chest here! \n"
            text += "A "+ self.chest.name + " has been found."
        return text

#    def __repr__(self):  # we're not using this yet
#        pass


    def describe(self):
        """ print full room description. """
        print(self)
    
    def exit(self, direction):
        """
        input: an exit direction, as string
        output: a Room object - either the room the player
            has moved to, or the current room if
            movement failed.
        """   
        pass 
        # I need access to the roomDict for this -- so it should 
        # go in Game, not Room.  
        
    def addItem(self, item):
        """ used to add item into a room"""
        self.add(item)
    
    def removeItem(self, item):
        if item in self.contents:
            self.remove(item)
        
    def addDoor(self, door, lockedexit):
        self.door = door
        self.lockedexit = lockedexit
        
    def addChest(self, chest):
        self.chest = chest
        
class Door():
    def __init__(self, name, description, state, locked, doorsid, keysid):
        self.name = name
        self.description = description
        self.state = state
        self.locked = locked
        self.doorsid = doorsid #test for master key match 
        self.keysid = keysid #test for key match 
    
    def look(self):
        print("Description: " + str(self.description))
        print("Locked: " + str(self.locked))
        print("doorid" + str(self.doorsid))
        print("keyid" + str(self.keysid))
    def open(self):
        self.state = 1
        self.description = "The door is open."
    def close(self):
        self.state = 0
        self.description = "The door is closed."
    def lock(self):
        self.locked = True
        print("The door is locked.")
    def unlock(self):
        self.locked = False
        print("The door is unlocked.")
    def exits(self):
        if self.locked == False:
            if self.state == 1:
                #door is passable
                return True
            else:
                print("Door is closed.")
                return False
        else:
            return False

class Chest(Container):
    def __init__(self, name, description, state, locked, chestsid, keysid):
        self.name = name
        self.description = description
        self.state = state
        self.locked = locked
        self.chestsid = chestsid
        self.keysid = keysid #test for key match
        self.contents = {}
        
    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = self.name + "\n"
        text += self.description + "\n"
        text += "Locked: " + str(self.locked) + "\n"
        # print items in room, if any
        if self.state == 0 and self.locked == True:
            text += "The chest is locked and closed and cant see anything."
        elif self.state == 0 and self.locked == False:
            text += "The chest is closed and cant see anything."
        else:
            if self.contents == {}:
                text += "There's no items here.\n"
            else:
                text += "In this chest you see: \n"
                text += self.listchestContents()
                # for item in self.contents:
                #     text += item.name + ": " + item.description + "\n"
        return text
    
    def look(self):
        print(self)
        # print("keyid" + str(self.keysid))
    def open(self):
        self.state = 1
    def unlock(self):
        self.locked = False
        print("The chest is unlocked.")
    
    def addItem(self, item):
        """ used to add item into a room"""
        self.add(item)
    
    def removeItem(self, item):
        if item in self.contents:
            self.remove(item)
    
def main():
    """Currently used for testing
    TODO: implement doctests"""
   
    bathroom = Room("Bath Room", "A room where you can take a bath/shower.",
                    {"east": "Save Room"})
    saveroom = Room("Save Room", "A safe bed room where you can save/load your progress, and respawn when dead.",
                    {"west": "Bath Room","south": "Living Room"})
    livingroom = Room("Living Room", "A room where kitchen, dining , and library are in 1 place.",
                      {"north": "Save Room","east": "Blacksmith Room", "west": "Magic/Enchant Room"})
    blacksmithroom = Room("Blacksmith Room", "You can craft items from raw materials and refine weapons to improve them here.",
                          {"west": "Living Room"})
    magicroom = Room("Magic/Enchant Room", "You can practice magic, or enchant your items, weapons, and armor.",
                     {"east": "Living Room"})
    
    
    # Place rooms in a dictionary.
    # (Game will handle this in the full version)
    roomDict = { bathroom.name: bathroom,
                    saveroom.name: saveroom,
                    livingroom.name: livingroom,
                    blacksmithroom.name: blacksmithroom,
                    magicroom.name: magicroom }
    
    chest1 = Chest("Chest","The chest is closed.", 0, True,200)
    saveroom.addChest(chest1)
    
    #Test out Items
    pizza = Item("Pizza", "A very fresh, hot pizza.")
    sword = Item("sword", "It's very sharp.")
    livingroom.addItem(pizza)
    blacksmithroom.addItem(sword)
    
    # Test out movement
    loc = saveroom
    print("Starting room:")
    loc.describe()
    
    print ("Heading West...")
    loc = roomDict[loc.exits["west"]] # find room to South, go there
    loc.describe()
    
    print ("Heading East...")
    loc = roomDict[loc.exits["east"]] # find room to North, go there
    loc.describe()
    
    print ("Heading South...")
    loc = roomDict[loc.exits["south"]] # find room to South, go there
    loc.describe()
    
    print ("Heading West...")
    loc = roomDict[loc.exits["west"]] # find room to North, go there
    loc.describe()
    
    print ("Heading East...")
    loc = roomDict[loc.exits["east"]] # find room to South, go there
    loc.describe()
    
    print ("Heading East...")
    loc = roomDict[loc.exits["east"]] # find room to North, go there
    loc.describe()
    
    print ("Heading West...")
    loc = roomDict[loc.exits["west"]] # find room to South, go there
    loc.describe()
    
    print ("Heading North...")
    loc = roomDict[loc.exits["north"]] # find room to North, go there
    loc.describe()

    # test chest
    # chest1 = Chest("Chest","The chest is closed.", 0, True)
    inv = []
    key = "key"
    while True:
            
        i = input("> ")
    
        if i == "get key":    
            if key in inv:
                print("You already have the key.")
            else:
                print("You pick up the key.")
                inv += [key]
                print(inv)
    
        elif i == "lock chest":
            if key not in inv:
                print("You do not have the key.")
            else:
                if chest1.state == 0 and chest1.locked == False:
                    chest1.lock()
                elif chest1.state == 0 and chest1.locked == True:
                    print("The chest is already locked.")
                elif chest1.state == 1:
                    print("You must first close the chest.")
                else:
                    print("You can't do that.")
                
        elif i == "unlock chest":
            if key not in inv:
                print("You do not have the key.")
            else:
                if chest1.state == 0 and chest1.locked == True:
                    chest1.unlock()
                elif chest1.state == 0 and chest1.locked == False:
                    print("The chest is already unlocked,")
                elif chest1.state == 1:
                    print("The chest is already unlocked and open.")
                else:
                    print("You can't do that.")
                
        elif i == "open chest":
            if chest1.state == 0:
                if chest1.locked == True:
                    print("The chest is locked.")
                elif chest1.locked == False:
                    chest1.open()
            else:
                print("The chest is already open.")
            
        elif i == "close chest":
            if chest1.state == 0:
                print("The chest is already closed.")
            else:
                chest1.close()
    
        elif i == "i":
            print(inv)
    
        elif i == "q":
            break
    
        else:
            print("I don't understand.")
            
        chest1.look()
    # test door
    ''' door1 = Door("Door","The door is closed.", 0, True,000,111)
    inv = []
    key = "key"
    print("You are in a room with a door. You see a key on the floor.")
    
    while True:
        
        i = input("> ")
    
        if i == "get key":    
            if key in inv:
                print("You already have the key.")
            else:
                print("You pick up the key.")
                inv += [key]
                print(inv)
    
        elif i == "lock door":
            if key not in inv:
                print("You do not have the key.")
            else:
                if door1.state == 0 and door1.locked == False:
                    door1.lock()
                elif door1.state == 0 and door1.locked == True:
                    print("The door is already locked.")
                elif door1.state == 1:
                    print("You must first close the door.")
                else:
                    print("You can't do that.")
                
        elif i == "unlock door":
            if key not in inv:
                print("You do not have the key.")
            else:
                if door1.state == 0 and door1.locked == True:
                    door1.unlock()
                elif door1.state == 0 and door1.locked == False:
                    print("The door is already unlocked,")
                elif door1.state == 1:
                    print("The door is already unlocked and open.")
                else:
                    print("You can't do that.")
                
        elif i == "open door":
            if door1.state == 0:
                if door1.locked == True:
                    print("The door is locked.")
                elif door1.locked == False:
                    door1.open()
            else:
                print("The door is already open.")
            
        elif i == "close door":
            if door1.state == 0:
                print("The door is already closed.")
            else:
                door1.close()
    
        elif i == "i":
            print(inv)
    
        elif i == "q":
            break
    
        else:
            print("I don't understand.")
            
        door1.look() '''
    

if __name__ == "__main__":
    main()