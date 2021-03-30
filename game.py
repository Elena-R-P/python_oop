class Ninja:
    def __init__(self, name, speed, attack_power, defense, ability, health):
        self.name = name
        self.speed = speed
        self.attack_power = attack_power
        self.defense = defense
        self.ability = ability
        self.health = health

    def attack(self, target, amount):
        target.health -= amount
        self.speed -= 10
        self.attack_power -= 20
        self.status()
        target.status()
        return self

    def status(self):
        print(
            f"Ninja {self.name} Speed: {self.speed}, attack_power: {self.attack_power}, defense: {self.defense}, health: {self.health}")
        if self.health < 10:
            print("Go to see a doctor!!!")
        return self


class Pirate:
    def __init__(self, name, speed, attack_power, defense, ability, health):
        self.name = name
        self.speed = speed
        self.attack_power = attack_power
        self.defense = defense
        self.ability = ability
        self.health = health

    def attack(self, target, amount):
        target.health -= amount
        self.speed -= 10
        self.attack_power -= 20
        self.status()
        target.status()
        return self

    def status(self):
        print(
            f"For Pirate {self.name} Speed: {self.speed}, attack_power: {self.attack_power}, defense: {self.defense}, health: {self.health}")
        if self.health < 10:
            print("Go to see a doctor!!!")
        return self

class Vik:
    def __init__(self, name, speed, attack_power, defense, ability, health):
        self.name = name
        self.speed = speed
        self.attack_power = attack_power
        self.defense = defense
        self.ability = ability
        self.health = health

    def attack(self, target, amount):
        target.health -= amount
        self.speed -= 10
        self.attack_power -= 20
        self.status()
        target.status()
        return self

    def status(self):
        print(
            f"For Vik {self.name} Speed: {self.speed}, attack_power: {self.attack_power}, defense: {self.defense}, health: {self.health}")

        if self.health < 10:
            print("Go to see a doctor!!!")
        return self


ninja1 = Ninja("Ciso", 70, 50, 70, "stealth", 100)
pirate1 = Pirate("Captain Jack", 30, 90, 20, "Cannon blast", 100)
viking = Vik("Ragnar", 40, 95, 60, "berzerk", 100)

viking.attack(pirate1, 50).attack(ninja1, 40)
ninja1.attack(pirate1, 50).attack(viking, 20)
pirate1.attack(viking, 40).attack(ninja1, 60)
