import random as rnd
import matplotlib.pyplot as plt

def data():
    path = {}

    print("What style of line would you like (:, -- or -)?")
    line_style = input()
    print("What colour should it be (r, g or b)?")
    colour = input()
    print("What style of marker (o, s or ^)?")
    marker = input()

    path.append(line_style, colour, marker)

    return data

def generate():
    print("How many line would you like to display?")
    lines = int(input())

    for line in range(lines):
        values = data()

        randomlist = []
        for number in range(2):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
            randomlist.append(x, y)
            plt.plot(x, y, format)

        plt.show()

def run():
  print("Running...")
  generate()
  print("Done!")


if __name__ == "__main__":
    run()