#Room Class

from Container import Container
from Item import Item

class Room(Container):
    """class for holding room names descriptions, exits"""       
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
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

    
    

if __name__ == "__main__":
    main()