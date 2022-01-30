import random
from planet import Planet
from robot import Robot
from human import Human
import matplotlib.pyplot as plt

class Universe:

    def __init__(self):
        self.planets = []

    def generate(self):
        planet = Planet()

        for i in range(random.randint(1,10)):
            robot = Robot(f"Robot{i}")
            planet.add_robot(robot)

        for i in range(random.randint(1,10)):
            human = Human(f"Human{i}")
            planet.add_human(human)

        self.planets.append(planet)

    def __repr__(self):
        return f"universe(planters={self.planets})."

    def __str__(self):
        return f"The universe contains {len(self.planets)} palnets."

    def show_populations(self):
        num_subplots = len(self.planets)

        fig = plt.figure()

        for index in range(num_subplots):
            planet = self.planets[index]
            num_humans = len(planet.inhabitants['humans'])
            num_robots = len(planet.inhabitants['robots'])

            ax = fig.add_subplot(1, num_subplots, index + 1)
            ax.bar([1, 2], [num_humans, num_robots])

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    universe = Universe()
    universe.generate()
    universe.generate()
    universe.show_populations()