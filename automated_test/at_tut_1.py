class Person:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def hit(self, target):
        target.hp -= self.damage

    def alive(self):
        return self.hp > 0