import items


class NPC():
    def __init__(self):
        raise NotImplementedError("Do not create raw Non Playable Character objects.")

    def __str__(self):
        return self.name


class Trader(NPC):
    def __init__(self):
        self.name = "Trading post"
        self.spaceCred = 100
        self.inventory = []
        
class RandomWeapon(NPC):
    def __init__(self):
        self.inventory = [items.Wrench(),
                          items.WeldingLaser(),
                          items.Phaser(),
                          items.RocketLauncher()]
        
class RandomHeals(NPC):
    def __init__(self):
        self.inventory = [items.Bandaid(),
                          items.HealingStim()]
