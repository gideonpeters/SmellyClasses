class RPGCharacter:
    def __init__(self, name, hp, attack_power, defense, level=1, exp=0):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = exp

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.hp -= damage

    def heal(self):
        self.hp = min(100, self.hp + 10)

    def gain_exp(self, exp):
        self.exp += exp
        while self.exp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= 100
        self.hp = 100 + 20 * (self.level - 1)
        self.attack_power = 20 + 5 * (self.level - 1)
        self.defense = 10 + 5 * (self.level - 1)

    def is_alive(self):
        return self.hp > 0
`