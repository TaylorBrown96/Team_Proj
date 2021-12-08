from Room import Room, Door, Chest
from Player import Player 
from Item import BaseItem, UsableItem, PuzzleItem
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
        saveroom = Room("Save Room", "A safe bed room where you can save/load your progress,\ and respawn when dead.", 
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
        
        
        world = Room("World", "WorldMap.",
                         {"east": "","south": "","east": ""})
        dungeon = Room("Dungeon", "WorldMap.",
                         {"east": ""})
        forest = Room("DeepForest", "WorldMap.",
                         {"east": ""})
        lakemarsh = Room("LakeMarsh", "WorldMap.",
                         {"east": ""})
        tombdungeon = Room("AncientTomb", "WorldMap.",
                         {"east": ""})
        #door initialize
        bathdoor = Door("BathDoor","The door is closed.", 0, False,0,111)
        frontdoor = Door("FrontDoor","The door is closed",0,True,0,112)
        #chest initialize
        enchantedchest = Chest("EnchantedChest","A sealed luxurious chest.", 0, True,250,251)
        craftchest = Chest("CraftChest","A chest with blacksmith materials.", 0, True,250,290)
        woodchest = Chest("WoodChest","A wooden decrepit chest.", 0, True,250, 299)
        
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
                    
                    world.name : world,
                    dungeon.name : dungeon,
                    forest.name : forest,
                    lakemarsh.name : lakemarsh,
                    tombdungeon.name : tombdungeon
                    }
        #Door Setup
        saveroom.addDoor(bathdoor,"west")
        bathroom.addDoor(bathdoor,"east")
        livingroom.addDoor(frontdoor, "south")
        house.addDoor(frontdoor,"north")
        #Chest Setup
        # saveroom.addChest(woodchest)#test
        saveroom.addChest(enchantedchest)#test
        blacksmithroom.addChest(craftchest)
        #item setup
        bed = BaseItem("bed", "A fluffy bed.")
        bed.canGet = False
        pizza = BaseItem("pizza", "A very fresh, hot pizza.")
        wand = UsableItem("wand","A stick with mystical energies.")
        sword = UsableItem("sword", "A long sword hanging on the wall.")
        
        
        bathroomkey = PuzzleItem("bathroomkey", "BathDoor to lock in ",111)
        frontkey = PuzzleItem("frontdoorkey", "Your house key",112)
        kingdomkey = PuzzleItem("kingdomkey", "A key to unlock any lock doors.",0)
        bronzechestkey = PuzzleItem("bronzechestkey","A key to unlock wood and bronzechests", 299)
        enchantedkey = PuzzleItem("enchantedkey","An unbreakable key that unlock chests", 250)
        bathroomkey.canDrop = False
        frontkey.canDrop = False
        kingdomkey.canDrop = False
        # item adding on rooms
        saveroom.addItem(bed)
        livingroom.addItem(frontkey)
        saveroom.addItem(bathroomkey)
        saveroom.addItem(enchantedkey)#test
        livingroom.addItem(pizza)
        saveroom.addItem(kingdomkey)
        blacksmithroom.addItem(sword)
        # item adding on chests
        enchantedchest.addItem(wand)
        # start room
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
        """
        # Command
        go (direction)
        look
        get (chest(optional))(item)
        drop (item)
        inv
        use(item)
        open (door/chest)
        close (door/chest)
        lock (door/chest)(itemkey)
        unlock (door/chest)(itemkey)
        """
        command = input(">")
        command = command.lower()
        words = command.split()
        #print(words)
        # try:
        if True:
            if len(words) < 1:
                print("No input detected")
                return
            
            verb = words[0]
            if verb == 'go':
                direction = words[1]
                self.commandGo(direction)
            elif verb == 'look':
                self.here.describe()
                if self.here.door != None:
                    self.here.door.look()
                if self.here.chest != None:
                    self.here.chest.look()
            elif verb == 'quit':
                self.isplaying = False
                print("Game Over!")
            elif verb == 'get':
                if len(words) == 2:
                    item = words[1]
                    self.commandGet(item)
                elif len(words) == 3:
                    item = words[2]
                    chest = words[1]
                    self.commandchestGet(chest, item)
            elif verb == 'drop':
                item = words[1]
                self.commandDrop(item)
            elif verb == 'inv':
                self.commandInv()
            elif verb == 'use':
                item = words[1]
                self.commandUse(item)
            elif verb == 'open':
                lid = words[1]
                self.commandOpen(lid)
            elif verb == 'close':
                lid = words[1]
                self.commandClose(lid)
            elif verb == 'lock':
                lid = words[1]
                item = words[2]
                self.commandLock(lid, item)
            elif verb == 'unlock':
                lid = words[1]
                item = words[2]
                self.commandUnlock(lid, item)
            
            
    
            else: # first word is verb
                print("I don't know how to ",words[0])
        # except:
        #     print("Action invalid/non-existent has been entered.")
    def commandGo(self, direction):
        """
        input: direction to move. 
        output: none
        side effect: player location is updated if possible
        """
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        
        if self.here.door != None: ##debug
            # print("There's a door blocking", self.here.lockedexit)
            # print("you're going", direction, "door is at", self.here.lockedexit)
            if self.here.lockedexit == direction:
                #print("the door should stop you if it's closed") debug
                # if self.here.door.state == 0: debug
                #     print("the door is closed.") debug
                # there's a door and it might be in our way
                if self.here.door.locked == True:
                    print("The door is locked.") 
                    print("There is a door on the way.")
                    return
                if self.here.door.state == 0:
                    print("The door is closed.")
                    print("There is a door on the way.")
                    return
            # if door is open and unlocked, go through!

        if self.here.exits.get(direction) != None: # this key does exist
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

    def commandchestGet(self, lid, itemName):
        """ remove the item from the room (if its there)
        and place it in player inventory
        """
        #TODO: actually do this
        #We'll need to remove the item from the current
        #rpp, and then add it to the inventory.
        chest = self.here.chest
        if lid == chest.name.lower():
            if chest != None:
                if chest.state == 1:
                    if chest.contents[itemName].canGet == False:
                        print(itemName,"cannot be picked up.")
                    else:
                        if chest.contents[itemName]:
                            item = chest.contents[itemName]
                            chest.moveItemTo(item, self.player)
                            print("You got the", itemName)
                            print(self.player.listContents())
                        else:
                            print("There's no ", itemName,"here.")
                else:
                    print("The chest is closed, open it first.")
            else:
                print("There is no chest here.")
        else:
            print("Get what chest??")
            
    def commandGet(self, itemName):
        """ remove the item from the room (if its there)
        and place it in player inventory
        """
        #TODO: actually do this
        #We'll need to remove the item from the current
        #rpp, and then add it to the inventory.
        if self.here.contents[itemName].canGet == False:
            print(itemName,"cannot be picked up.")
        else:
            if self.here.contents[itemName]:
                item = self.here.contents[itemName]
                self.here.moveItemTo(item, self.player)
                print("You got the", itemName)
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
        
        if self.here.contents[itemName].canDrop == False:
            print(itemName,"cannot be picked up.")
        else:
            if self.player.contents[itemName]:
                item = self.player.contents[itemName]
                self.player.moveItemTo(item, self.here)
                print("You drop the", itemName,".")
            else:
                print("You don't have the", itemName,"to drop.")
        
    def commandInv(self):
        # self.player.Inventory()
        for item in self.player.contents:
            print(item) 
    
    def commandUse(self, itemName):
        if self.player.contents[itemName]:
            items = self.player.contents[itemName]
            items.use()
            print("You used the", itemName,".")
            print(self.player.listContents())
        else:
            print("You don't have the", itemName,"in your inventory.")
    def commandOpen(self, lid):
        door = self.here.door
        chest = self.here.chest
        if lid == door.name.lower():
            if door != None:
                if door.state == 0:
                    if door.locked == True:
                        print("The door is locked.")
                    elif door.locked == False:
                        door.open()
                        door.look() #check the door state
                else:
                    print("The door is already open.")
        elif lid == chest.name.lower():
            if chest != None:
                if chest.state == 0:
                    if chest.locked == True:
                        print("The door is locked.")
                    elif chest.locked == False:
                        chest.open()
                        chest.look() #check the chest state
                else:
                    print("The door is already open.")
        else:
            print("I don't understand.")
    def commandClose(self, lid):
        door = self.here.door
        if lid == door.name.lower():
            if door != None:
                if door.state == 0:
                    print("The door is already closed.")
                else:
                    door.close()
                    door.look() #check the door state
        else:
            print("I don't understand.")
    def commandUnlock(self, lid, itemName):
        chest = self.here.chest
        door = self.here.door
        item = self.player.contents[itemName]
        if lid == door.name.lower():
            if door != None:
                if item.name in self.player.contents:
                    print(item)
                    if item.itemsid == door.doorsid:
                        
                        if door.state == 0 and door.locked == True:
                            door.unlock()
                            door.look() #check the door state
                        elif door.state == 0 and door.locked == False:
                            print("The door is already unlocked,")
                        elif door.state == 1:
                            print("The door is already unlocked and open.")
                        else:
                            print("You can't do that.")
                    elif item.itemsid == door.keysid:
                        
                        if door.state == 0 and door.locked == True:
                            door.unlock()
                            door.look() #check the door state
                        elif door.state == 0 and door.locked == False:
                            print("The door is already unlocked,")
                        elif door.state == 1:
                            print("The door is already unlocked and open.")
                        else:
                            print("You can't do that.")
                    else:
                        print("Wrong key.")
        elif lid == chest.name.lower():
            if chest != None:
                if item.name in self.player.contents:
                    print(item)
                    if item.itemsid == chest.chestsid:
                        if chest.state == 0 and chest.locked == True:
                            chest.unlock()
                            chest.look()
                            if item.name == 'enchantedkey':
                                print(item.name," has been used.")
                                print(item.name," is unbreakable.")
                        elif chest.state == 0 and chest.locked == False:
                            print("The chest is already unlocked,")
                        elif chest.state == 1:
                            print("The chest is already unlocked and open.")
                        else:
                            print("You can't do that.")
                    elif item.itemsid == chest.keysid:
                        if chest.state == 0 and chest.locked == True:
                            chest.unlock()
                            chest.look()
                            print(item.name," has been broken after use.")
                            self.player.deleter(item)
                        elif chest.state == 0 and chest.locked == False:
                            print("The chest is already unlocked,")
                        elif chest.state == 1:
                            print("The chest is already unlocked and open.")
                        else:
                            print("You can't do that.")
        else:
            print("I don't understand.")
    def commandLock(self, lid, itemName):
        door = self.here.door
        item = self.player.contents[itemName]
        if lid == door.namelower():
            if door != None:
                if item.name in self.player.contents:
                    print(item)
                    #print("You tried to lock,", doorName)
                    if item.itemsid == door.doorsid:
                    
                        if door.state == 0 and door.locked == False:
                            door.lock()
                            door.look() #check the door state
                        elif door.state == 0 and door.locked == True:
                            print("The door is already locked.")
                        elif door.state == 1:
                            print("You must first close the door.")
                        else:
                            print("You can't do that.")
                    elif item.itemsid == door.keysid:
                        if door.state == 0 and door.locked == False:
                            door.lock()
                            door.look() #check the door state
                        elif door.state == 0 and door.locked == True:
                            print("The door is already locked.")
                        elif door.state == 1:
                            print("You must first close the door.")
                        else:
                            print("You can't do that.")
                    else:
                        print("Wrong key.")
        else:
            print("I don't understand.")
    
    
def main():
    game = Game()
    game.setup()
    print("Starting game -- enter command")
    game.loop()
    game.end()
    
if __name__ == "__main__":
    main()