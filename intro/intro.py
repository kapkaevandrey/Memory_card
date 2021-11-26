class Person:
    def __init__(self, name, power, skill):
        self.name = name
        self.power = power
        self.skill = skill
        self.health = 100

    def add_damage(self):
        print(f"Damage {self.power}")
        return self.power

    def get_damage(self, damage):
        print("Get damage")
        self.health -= damage


class Barbarian(Person):
    def __init__(self, name, power, skill):
        super().__init__(name, power, skill)
        self.health *= 2
        self.color_hair = "Black"

    def add_double_damage(self):
        print(f"Damage {self.power * 2}")
        return self.power * 2


pudge = Person(name="Pudge", power=20, skill=10)
conan = Barbarian(name="Conan", power=50, skill=5)
