from Player import Player
from Room import Room
from Item import BaseItem, UsableItem, PuzzleItem
from Game import Game


class MyGame(Game):
    """The game class should be subclassed to add
    game specific features, including the world setup
    """
    def setup(self):
        """ Loading your rooms in the method of your choice.
        Considere a gameloader class that might read these
        from a file...
        """
        loader = MyGameLoader()
        self.rooms = loader.setup()
        
        self.here  = self.rooms["Save Room"]
        
        self.here.describe()#Turn 1 look

class MyGameLoader:
    """ just used to put all the room setup in a separate class,
    and if needed, a separate files."""
    
    def setup(self):
        """ Create the rooms and initialize everything."""
        bathroom = Room("BathRoom", "A room where you can take a bath/shower.",
                        {"east": "Save Room"})
        saveroom = Room("Save Room", "A safe bed room where you can save/load your progress, and respawn when dead.",
                        {"west": "BathRoom","south": "LivingRoom"})
        livingroom = Room("LivingRoom", "A room where kitchen, dining , and library are in 1 place.",
                          {"north": "Save Room","east": "Blacksmith Room", "west": "Magic/Enchant Room"})
        blacksmithroom = Room("Blacksmith Room", "You can craft items from raw materials and refine weapons to improve them here.",
                              {"west": "LivingRoom"})
        magicroom = Room("Magic/Enchant Room", "You can practice magic, or enchant your items, weapons, and armor.",
                         {"east": "LivingRoom"})
        
        rooms = { bathroom.name: bathroom,
                    saveroom.name: saveroom,
                    livingroom.name: livingroom,
                    blacksmithroom.name: blacksmithroom,
                    magicroom.name: magicroom }
        #item setup
        pizza = BaseItem("Pizza", "A very fresh, hot pizza.")
        sword = UsableItem("sword", "A longsword hanging on the wall.")
        livingroom.addItem(pizza)
        blacksmithroom.addItem(sword)
        
        return rooms


def main():
    game = MyGame()
    game.setup()
    game.output("Starting game -- enter command.")
    game.Loop()
    game.end()