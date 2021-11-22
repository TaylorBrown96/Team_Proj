#####
# class Item:
#     """
#     Items are found in rooms, or in the player inventory.
#     (Possibly we'll change that to being found in Container objects?)
     
#     They may be used to solve puzzles, give points to score, etc.
#     """
     
#     def __init__(self, name, description):
#          self._name = name
#          self._description = description
        
#         #Setting Basic Flag commands for the Base items to be inherited
#          self._canGet = True #default to gettable/ pick up 
#          self._canDrop = True #The drop id to see if items can be dropped.
         
#     def __str__(self):
#         return self._name + " : " + self._description
    
#     @property 
#     def name(self):
#         return self._name
    
#     @property 
#     def description(self):
#         """Returning the decorated descriptions for an item
#         For example when an item is too heavy to lift. This way players
#         cannot simply pick up every item and put into their inventory"""
#         desc = self._description
#         if self._canGet == False:
            
      
#     @property 
#     def canGet(self):
#         return self._canGet
    
#     @canGet.setter 
#     def canGet(self, setting):
#         """The true/false setting for an item if it can be picked up"""
#         self._canGet = setting
        
#     @property 
#     def canDrop(self):
#         return self._canDrop
    
#     @canDrop.setter 
#     def canDrop(self, setting):
#         """This will be the true/false setting for if an item can be dropped
#             or not"""
#         self._canDrop = setting
#####

###
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "A pocket knife, good for self-defence."
        self.damage = 5
        self.value = 1


class NailGun(Weapon):
    def __init__(self):
        self.name = "Nail Gun"
        self.description = "An old abandoned nail gun, surprisingly servicable."
        self.damage = 10
        self.value = 15


class Chainsaw(Weapon):
    def __init__(self):
        self.name = "Chainsaw"
        self.description = "A well-maintained chainsaw, might be more effective"\
            "than your current weapon."
        self.damage = 20
        self.value = 25

'''
class (Weapon):
    def __init__(self):
        self.name = ""
        self.description = ""
        self.damage = 30
        self.value = 50
'''
class LasGun(Weapon):
    def __init__(self):
        self.name = "LasGun"
        self.description = "Does a ton of damage, no recoil and lookin' cool doing it."
        self.damage = 70
        self.value = 100

###
class Armor:
    def __init__(self):
        raise NotImplementedError("Do not create raw Armor objects.")

    def __str__(self):
        return self.name

class StandardArmySuit(Armor):
    def __init__(self):
        self.name = "Test Armor"
        self.description = "A test armor for damage reduction stuff"
        self.reduction = 0.8 # 20% reduction
        self.value  = 20

    def damage_reduction(self):
        reduction = self.reduction
        return reduction


###
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class Bandaid(Consumable):
    def __init__(self):
        self.name = "Bandaid"
        self.healing_value = 10
        self.value = 20


class HealingStim(Consumable):
    def __init__(self):
        self.name = "Healing Stim"
        self.healing_value = 50
        self.value = 60



###
class PuzzlePiece:
    def __init__(self):
        raise NotImplementedError("Do not create raw Puzzle Piece objects.")

    def __str__(self):
        return "{}".format(self.name)

class KeyCard(PuzzlePiece):
    def __init__(self):
        self.name = "Key"
        self.value = 10

class Key(PuzzlePiece):
    def __init__(self):
        self.name = "Key"
        self.value = 10
        
#####
# class Container(UseableItem, EquiptableItem):
#     """The main holding container class that can be holding either useable,
#     or equipable items in this case. This class will be modified in the future"""
#     def __init__(self, name, description):
#          super().__init__(name,description)
#          self.contents = []
#          self.open = False
#          self.locked = False
#          self.key = False
#          self.enterable = False
        
# class lockedDoor(Container):
#     def __init__(self,name,description):
#         self.open = False
#         self.locked = True
#         self.key = True
#         self.enterable = True
####