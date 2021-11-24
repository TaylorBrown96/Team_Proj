
class Item:
    """
    Items are found in rooms, or in the player inventory.
    (Possibly we'll change that to being found in Container objects?)
     
    They may be used to solve puzzles, give points to score, etc.
    
    This is the base class, which only supports get, drop, and examine
    """
     
    def __init__(self, name, description):
         self._name = name
         self._description = description
         
         # set basic flags
         self._canGet = True # default to gettable
         
    def __str__(self):
        return self.name + " : " + self.description
    
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        """return a decorated description. 
        Decoration = things like (too heavy to lift)""" 
        desc = self._description
        # decorate with extra info as needed
        if self.canGet == False:
            desc += " It's too heavy to lift."
        return desc
                 
                 
    @property 
    def canGet(self):
        """ True / False -- item can be picked up. """
        return self._canGet
    
    @canGet.setter 
    def canGet(self, setting):
        """ True / False - item can be picked up. """
        self._canGet = setting



#test code
def main():
    key = Item("key", "It's a bit rusty.")
    
    sword = Item("sword", "It's very sharp.")
    
    stuff = [key,sword]
    for item in stuff:
        print(item)
    
    
    
if __name__ == "__main__":
    main()