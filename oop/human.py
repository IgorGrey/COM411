class Human:

    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    def grow(self, amount):
        if self.energy + amount <= Human.MAX_ENERGY:
            self.energy = self.energy + amount
        else:
            self.energy = Human.MAX_ENERGY

    def move(self, distance):
        if self.energy >= distance:
            self.energy = self.energy - distance
        else:
            self.energy = 0

    def display(self):
        print(f"I am {self.name}, {self.age} years old, and with {self.energy} energy")

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'


if __name__ == "__main__":

    human = Human()
    human.display()
