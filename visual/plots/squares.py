import matplotlib.pyplot as plt


def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]
    plt.plot(x, y, 'r:o')

def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    plt.plot(x, y, 'g--s')

def large():
    x = [1, 6, 6]
    y = [6, 6, 1]
    plt.plot(x, y, 'b-p')

def run():
    small()
    medium()
    large()
    plt.show()


if __name__ == "__main__":
    run()