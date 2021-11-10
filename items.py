

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Wrench(Weapon):
    def __init__(self):
        self.name = "Wrench"
        self.description = "A size 21mm wrench, might be good against an enemy."
        self.damage = 5
        self.value = 1


class WeldingLaser(Weapon):
    def __init__(self):
        self.name = "Welding Laser"
        self.description = "This might be good against the aliens exo-armour."
        self.damage = 10
        self.value = 15


class Phaser(Weapon):
    def __init__(self):
        self.name = "Phaser"
        self.description = "Shoots red beams of light that are 10 million degrees."
        self.damage = 20
        self.value = 50


class RocketLauncher(Weapon):
    def __init__(self):
        self.name = "Rocket Launcher"
        self.description = "Does a ton of damage but it costs alot of creds"
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