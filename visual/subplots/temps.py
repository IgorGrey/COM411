import matplotlib.pyplot as plt

def read_data(file_path):
    temps = []
    with open(file_path) as file:
        for line in file:
            temps.append(float(line.strip()))
    return temps

def run():
    data = read_data('temps.txt')
    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    plt.show()

if __name__ == "__main__":
    run()