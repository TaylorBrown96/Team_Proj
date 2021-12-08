
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
         self._canDrop = True
         
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
        return self._canGet
    
    @canGet.setter 
    def canGet(self, setting):
        """ True / False - item can be picked up. """
        self._canGet = setting

    @property 
    def canDrop(self):
        return self._canDrop
    
    @canDrop.setter 
    def canDrop(self, setting):
        """This will be the true/false setting for if an item can be dropped
            or not"""
        self._canDrop = setting
        
class BaseItem(Item):
     """
     This inherits from BaseItem. 
     We'll discuss how init(), etc. work as we go.
     """
     def __init__(self, name, description):
        # "super" runs the equiv function from the base class
        super().__init__(name, description) 
        
class UsableItem(BaseItem):
    """
    Works like a regular item, except that
    it has one or more usable verbs
    that will cause it to make changes.
    """    
    def __init__(self, name, description):
        super().__init__(name, description)
        # item is "unused" by default
        self._wasUsed = False
        
    def use(self, useVerb = "use"):
        """
        use() - call to make the object 
        change to its other state.
        TODO: this needs more development

        Parameters
        ----------
        useVerb : TYPE, optional
            DESCRIPTION. The default is "use".

        Returns
        -------
        None.

        """
        if self._wasUsed == True:
            print("You already used this item.")
        else:
            print("You attempt to",useVerb,"the item.")
            self._wasUsed = True
        
    
    @property
    def description(self):
        """return a decorated description. 
        Decoration = things like (too heavy to lift)
        """ 
        
        """Example code bellow"""
        # desc = self._description
        # # decorate with extra info as needed
        # if self._wasUsed == True:
        #     desc += " It's very shiny."
        # else:
        #     desc += " It's pretty rusty."
        # return desc

class PuzzleItem(BaseItem):
    def __init__(self, name, description, itemsid):
        super().__init__(name, description)
        self.itemsid = itemsid # test for key match

#test code
def main():
    key = PuzzleItem("key", "It's a bit rusty.", '111')
    
    sword = UsableItem("sword", "just a long sword.")
    
    bed = BaseItem("bed", "A fluffy bed.")
    bed.canGet = False
    
    stuff = [key,sword, bed]
    for item in stuff:
        print(item.name, "-", item.description)
    print()
    sword.use()
    for item in stuff:
        print(item.name, "-", item.description)
    
    if key.itemid == "111":
        print("key match")
    else:
        print("key doesn't match")
        
    if key.itemid == "112":
        print("key match")
    else:
        print("key doesn't match")
    
if __name__ == "__main__":
    main()