from Room import Room
from Player import Player 
from Item import Item
from Container import Container
# Game - Holds Game code

class Game:
    """ class that manages the entire game """
    
    def __init__(self):
        """ Initialize object (with no rooms) """
        self.rooms = { } # stored in dictionary
        # self.here = None # TODO: move this to Player#
        # Player is used to store location(loc) and etc.
        self.player = Player()
        
        self.isplaying = True
        self.isVerbose = True # auto-look on move

    def __str__(self):
        pass

    def __repr__(self):
        pass
    
    def setup(self):
        """ Create the rooms and initialize everything."""
        bathroom = Room("BathRoom", "A room where you can take a bath/shower.",
                        {"east": "Save Room"})
        saveroom = Room("Save Room", "A safe bed room where you can save/load your progress,\
                        and respawn when dead.", 
                        {"west": "BathRoom","south": "LivingRoom"})
        livingroom = Room("LivingRoom", "A room where kitchen, dining , and \
                          library are in 1 place.",
                          {"north": "Save Room","east": "Blacksmith Room", 
                           "west": "Magic/Enchant Room","south": "Outside House"})
        blacksmithroom = Room("Blacksmith Room", "You can craft items from raw \
                              materials and refine weapons to improve them here.",
                              {"west": "LivingRoom"})
        magicroom = Room("Magic/Enchant Room", "You can practice magic, or \
                         enchant your items, weapons, and armor.",
                         {"east": "LivingRoom"})
        
        #TownMap
        house = Room("Outside House", "Your house where you live.",
                        {"north": "LivingRoom", "east": "Town Center"})
        towncenter = Room("Town Center", "The town center where you live and,\
                          a gathering of civilization for adventuring, \
                              socializing, and profit.",
                        {"east": "Bazaar","west": "Outside House",
                         "south": "Town Gate"})
        bazaar = Room("Bazaar", "General shop for your adventuring needs: potion,\
                      bandage, food, ingredients, etc. etc. .",
                          {"north": "MerchantBuyer","east": "Wizard Shop", 
                           "west": "Town Center"})
        noblemerchantarea = Room("MerchantBuyer", "Noble's area of residence\
                                 where a rich noble merchant buys a rare\
                                     strange of items from the dungeon.",
                              {"South": "Bazaar"})
        wizardshop = Room("Wizard Shop", "Wizard shop that sells magic scrolls, recipies,\
                          magic ingredients, rare potions for temp. boosts.",
                              {"west": "Bazaar"})
        towngate = Room("Town Gate", "This is the gate to the outside world \.",
                         {"north": "Town Center","south":"World"})
        
        world = Room("World", "\.",
                         {"east": ""})
        
        
        self.rooms = { bathroom.name: bathroom,
                    saveroom.name: saveroom,
                    livingroom.name: livingroom,
                    blacksmithroom.name: blacksmithroom,
                    magicroom.name: magicroom,
                    
                    house.name : house,
                    towncenter.name : towncenter,
                    bazaar.name : bazaar,
                    noblemerchantarea.name : noblemerchantarea,
                    wizardshop.name : wizardshop,
                    towngate.name : towngate,
                    world.name : world }
        #item setup
        pizza = Item("pizza", "A very fresh, hot pizza.")
        sword = Item("sword", "Recently forged, and it's very sharp.")
        livingroom.addItem(pizza)
        blacksmithroom.addItem(sword)
        
        self.here  = saveroom
        
        self.here.describe()#Turn 1 look
        
    def loop(self):
        """ until the player quits, wins or loses, keep playing """
        self.isplaying = True
        while self.isplaying:
            self.playerAction()
        print("Bye!!")
    def end(self):
        """ say goodbye and do any cleanup needed """
        pass
    
    def playerAction(self):
        command = input(">")
        command = command.lower()
        words = command.split()
        #print(words)
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == 'go':
            direction = words[1]
            self.commandGo(direction)
            """
            # CommandGo relocate
            # # Can we go in the chosen direction from here?
            # if self.player.loc.exits.get(direction) == None:
            #     print("You can't go that way.")
            # else: # this key does exist
            #     newRoomName = self.player.loc.exits[direction]
            #     newRoom = self.rooms[newRoomName]
            #     self.player.loc = newRoom
            #     if self.isVerbose:
            #         self.player.loc.describe()
            """
        elif verb == 'look':
            self.here.describe()
        elif verb == 'quit':
            self.isplaying = False
            print("Game Over!")
        elif verb == 'get':
            item = words[1]
            self.commandGet(item)
        elif verb == 'drop':
            item = words[1]
            self.commandDrop(item)
        elif verb == 'inv':
            self.commandInv()

        else: # first word is verb
            print("I don't know how to ",words[0])
            
    def commandGo(self, direction):
        """
        input: direction to move. 
        output: none
        side effect: player location is updated if possible
        """
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else: # this key does exist
            newRoomName = self.here.exits[direction]
            newRoom = self.rooms[newRoomName]
            self.here = newRoom
            self.here.describe()
        #Helper functions - not necessary but useful
        @property
        def here(self):
            return self.player.loc
        @here.setter
        def here(self, room):
            self.player.loc = room
            
    def commandGet(self, itemName):
        """ remove the item from the room (if its there)
        and place it in player inventory
        """
        #TODO: actually do this
        #We'll need to remove the item from the current
        #rpp, and then add it to the inventory.
        #ITEM DUPE
        if self.here.contains(itemName):
            item = self.here.contents[itemName]
            self.here.moveItemTo(item, self.player.contents)
            print("You got the ", itemName)
            print(self.player.listContents())
        else:
            print("There's no ", itemName,"here.")
        
    def commandDrop(self, itemName):
        """ remove the item from the player 
        (if its there) and place it in the room
        """
        #TODO: actually do this
        #We'll need to remove the item from the current
        #rpp, and then add it to the inventory.
        
        if self.player.contains(itemName):
            item = self.player.contents[itemName]
            self.player.moveItemTo(item, self.here)
            print("You drop the", itemName,".")
        else:
            print("You don't have the", itemName,"to drop.")
        
    def commandInv(self):
        # self.player.Inventory()
        for item in self.player.contents:
            print(item)
        
def main():
    game = Game()
    game.setup()
    print("Starting game -- enter command")
    game.loop()
    game.end()
    
if __name__ == "__main__":
    main()