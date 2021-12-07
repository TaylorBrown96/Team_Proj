#Creation of the Container Classes for the game engine
# Using existing code that is already created and modifying it for the purposes of fitting the game engine
# These will be the attempts made and shall be used with a test code feature.


from item import Item

class Container: 
    """This is the class that hands collection of items"""

    def __init__(self):
        self.contents = {}

    def add(self, Item):
        self.contents[item.name] = Item

    def remove(self, Item):
        if self.contains(item.name):
            self.contents.remove(item)
    
    def moveItemto(self, item, desitnation):
        desitnation.add(item)
        self.remove(item)

    
    def contains(self, item):
        """Purpose for this function is to see if the item is in the inventory"""
        itemList = list(self.contents.item)
