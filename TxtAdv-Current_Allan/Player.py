from Container import Container
from Item import Item

class Player(Container):
    """
    Any data relating to the player himself should go in
    the Player class.
    Ex: location, inventory, health status, etc. etc.
    """
    def __init__(self):
        self.loc = None #what room is the player in
        self.hp = 100
        self.currency = 50
        self.victory = False
        
        self.contents = {} # because we're also a container
    
    def is_alive(self):
        return self.hp > 0
    
    