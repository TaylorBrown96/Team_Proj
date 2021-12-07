#This is the item class for creating items.

class Item:
    """
    Items are found in rooms, or in the player inventory.
    (Possibly we'll change that to being found in Container objects?)
     
    They may be used to solve puzzles, give points to score, etc.
    """
     
    def __init__(self, name, description):
         self._name = name
         self._description = description
        
        #Setting Basic Flag commands for the Base items to be inherited
         self._canGet = True #default to gettable/ pick up 
         self._canDrop = True #The drop id to see if items can be dropped.
         
    def __str__(self):
        return self._name + " : " + self._description
    
    @property 
    def name(self):
        return self._name
    
    @property 
    def description(self):
        """Returning the decorated descriptions for an item
        For example when an item is too heavy to lift. This way players
        cannot simply pick up every item and put into their inventory"""
        desc = self._description
        if self._canGet == False:
            
   
    @property 
    def canGet(self):
        return self._canGet
    
    @canGet.setter 
    def canGet(self, setting):
        """The true/false setting for an item if it can be picked up"""
        self._canGet = setting
        
    @property 
    def canDrop(self):
        return self._canDrop
    
    @canDrop.setter 
    def canDrop(self, setting):
        """This will be the true/false setting for if an item can be dropped
            or not"""
        self._canDrop = setting
        
class ConsumableItem(Item):
    """This is the function that will inherit from the Item class, and 
        should have a limit to what it can do"""
    
    def __init__(self, name, description):
        super().__init__(name, description)
            
        
    #def consumableCount():
            """This handles the number of consumables using a dictionary
                and removing duplicate items and appending as a number
                for example [dollar, dollar, dollar] would change to dollar(3)"""
            #The command prompt in case it is actually need to test
            #Not every sure if it is necessary but will keep it for the time being
            #The goal of the function is to create of items, keep a count, and
            #Most likely doesn't need to be refactored. But done so for clearty
            #Will fix this part asap and might not do the refactoring.
            self.consumeable = int
            self.count = 0
            #consumableCount = int
            #consumable = []
            
            # command = input(">")
            # command = command.lower()
            # words = command.split() # spliting the white space.
            # if len(words) < 1:
            #     print("No input detected")
            #     return 
            
             
            #for item in consumable:
                #if item in consumbleCount.keys():
                    #consumableCount[item] += 1
                #else:
                    #consumableCount[item] = 1
                    
            
        #This next part might not work as intended as the inventory
        #has not been fully implented so it will be commented out
        #Until the inventory is created, leaving it as place holder
        #for a todo issue.
            # for item in set(inventory):
            #     if consumableCount[item] > 1:
            #         print(' %s (%s)' % (item, cosnumableCount[item]))
            #     else:
            #         print(' ' + item)
        
        
    def consumableRemoval():
            consumeable = int
            if consumeable > 0:
                print("You have used", item)
                count += -1
            elif consumeable == 0:
                print("You used your last", item)
                count = 0
            else:
                print("You can't use that")
        
    
    
class EquiptableItem(Item):
    """This Function handles the items in which can be equipped to a character
        which can be moved from the player to the inventory"""
        def __init__(self, name, description):
             super().__init__(name, description)
             self.wearable = True
             self.concealed = False
             self.fixed = False
            
class LlamaPistol(EquiptableItem):
    def __init__(self, name, description):
       super().__init__(name, description)
       self.wearable = True
       self.concealed = True
       self.fixed = False
       self.ammo = 12
       self.damage = 20
        
class SurvivalKnife(EquiptableItem):
    def __init__(self,name,decription):
    super().__init__(name, description)    
        self.wearable = True
        self.concealed = True
        self.fixed = False
        self.damage = 10
    
class Container(UseableItem, EquiptableItem):
    """The main holding container class that can be holding either useable,
    or equipable items in this case. This class will be modified in the future"""
    def __init__(self, name, description):
         super().__init__(name,description)
         self.contents = []
         self.open = False
         self.locked = False
         self.key = False
         self.enterable = False
        
class lockedDoor(Container):
    def __init__(self,name,description):
    super().__init__(name, description)
        self.open = False
        self.locked = True
        self.key = True
        self.enterable = True
        
class deadBody(Container):
    def __init__(self,name,descripton)
    super().__init__(name, description)
        self.contents = [keyCard]
        
class briefCase(Container):
    def __init__(self,name,description)
    super().__init__(name, description)    
        self.contents = [Argentinan Peso(),
                         Nuclear Codes(),
                         Mission Documents(),
                         Agent ID Badge(),
                         Spare Pistol Mag(),
                         Passport(),
                         Strange Transmittor()]
        self.open = False
        self.enteratable = False
   
        
    

     
