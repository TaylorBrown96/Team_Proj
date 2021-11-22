

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


class PuzzlePiece:
    def __init__(self):
        raise NotImplementedError("Do not create raw Puzzle Piece objects.")

    def __str__(self):
        return "{}".format(self.name)


class Key(PuzzlePiece):
    def __init__(self):
        self.name = "Key"
        self.value = 10