class Human:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}, {self.age} years old, and with {self.energy} energy")


if __name__ == "__main__":

    human = Human()
    human.display()

class Robot:

    max_energy = 0

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = 100

    def display(self):
        print(f"I am {self.name}, {self.age} years old, and with {self.energy} energy")


if (__name__ == "__main__"):

    robot = Robot()
    robot.display()