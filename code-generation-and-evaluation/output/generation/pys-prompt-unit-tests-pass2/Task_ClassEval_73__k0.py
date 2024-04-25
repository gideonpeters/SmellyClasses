class RPGCharacter:
    def __init__(self, name, hp, attack_power, defense, level=1, exp=0):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = exp

    def attack(self, target):
        target.hp -= self.attack_power

    def heal(self):
        self.hp = min(self.hp + 10, 100)

    def gain_exp(self, exp):
        self.exp += exp
        while self.exp >= 100:
            self.level += 1
            self.exp -= 100

    def level_up(self):
        if self.level < 100:
            self.level += 1
            self.hp += 20
            self.attack_power += 5
            self.defense += 5

    def is_alive(self):
        return self.hp > 0
