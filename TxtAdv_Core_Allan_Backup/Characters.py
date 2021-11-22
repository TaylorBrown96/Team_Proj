import items


class NPC():
    def __init__(self):
        raise NotImplementedError("Do not create raw Non Playable Character objects.")

    def __str__(self):
        return self.name
#Character creation NPC 
class Survivor(NPC):
    def __init__(self):
        self.name = "Survivor"
        self.currency = 100
        self.inventory = [items.HealingStim()]

class Trader(NPC):
    def __init__(self):
        self.name = "Trading post"
        self.currency = 100
        self.inventory = []
        
class RandomWeapon(NPC):
    def __init__(self):
        self.inventory = [items.Knife(),
                          items.NailGun(),
                          items.Chainsaw(),
                          items.LasGun()]
        
class RandomHeals(NPC):
    def __init__(self):
        self.inventory = [items.Bandaid(),
                          items.HealingStim()]
