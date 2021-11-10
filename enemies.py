class Enemy:
    def __init__(self):
        raise NotImplementedError("DO not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class FaceSucker(Enemy):
    def __init__(self):
        self.name = "Face Sucker"
        self.hp = 10
        self.damage = 2


class WorkerAlien(Enemy):
    def __init__(self):
        self.name = "Worker Alien"
        self.hp = 30
        self.damage = 10


class SoldierAlien(Enemy):
    def __init__(self):
        self.name = "Soldier Alien"
        self.hp = 100
        self.damage = 4


class MotherAlien(Enemy):
    def __init__(self):
        self.name = "Mother Alien"
        self.hp = 80
        self.damage = 15