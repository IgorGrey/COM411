import matplotlib.pyplot as plt


def coordinate():
    print("Please enter the value for x:")
    x = int(input())
    print("Please enter the value for y:")
    y = int(input())

    return x, y


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for iteration in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]


def run():
    values = path()
    plt.plot(values[0], values[1], "r--o")
    plt.show()


if __name__ == "__main__":
    run()
