import random

class Enemy:
    def __init__(self):
        raise NotImplementedError("DO not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

# class (Enemy):
#     def __init__(self):
#         self.name = ""
#         self.hp = 10
#         self.damage = 2

class Mimic(Enemy):
    def __init__(self):
        self.name = "Mimic"
        self.hp = 10
        self.damage = 0
        
    def changeState(self):
        temp_chance = random.randint(0,100)
        if temp_chance <= 25:
            self.hp = 10
            self.damage = 20
        elif temp_chance >= 75:
            self.hp = 0
            self.damage = 0
            self.state


class Spider(Enemy):
    def __init__(self):
        self.name = "Spider"
        self.hp = 10
        self.damage = 2


class InfectedHuman(Enemy):
    def __init__(self):
        self.name = "Infected Human"
        self.hp = 30
        self.damage = 10


class Brute(Enemy):
    def __init__(self):
        self.name = "Brute"
        self.hp = 100
        self.damage = 4


class FlowerSource(Enemy):
    def __init__(self):
        self.name = "Mother Alien"
        self.hp = 80
        self.damage = 15