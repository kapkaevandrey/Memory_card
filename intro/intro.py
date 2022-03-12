from random import randint

class Person:
    def __init__(self, name, attack, health):
        self.attack = attack
        self.name = name
        self.health = health

    def add_damage(self):
        print(f"{self.name} add {self.attack} damage!")
        return self.attack

    def get_damage(self, damage):
        print(f"{self.name} get {damage} damage!")
        self.health -= damage


class Assasin(Person):
    def __init__(self, name, attack, health):
        super().__init__(name, attack, health)
        self.attack *= 2

    def kill_moment(self):
        print(f"{self.name} kill you!")
        return self.attack * 100

    def get_damage(self, damage):
        damage *= randint(0, 1)
        super().get_damage(damage)


spike = Person(name="Spike", attack=20, health=100)
ecio = Assasin(name="Ecio Auditore", attack=10, health=50)