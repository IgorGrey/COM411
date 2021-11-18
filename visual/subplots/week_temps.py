import csv
import matplotlib.pyplot as plt

def read_data():
    with open('temps.csv') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = {'week1': [], 'week2': []}

        for line in csv_reader:
            data['week1'].append(float(line[0].strip()))
            data['week2'].append(float(line[0].strip()))

    return data

def run():
    data = read_data()

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data['week1'])), data['week1'])
    ax2.plot(range(len(data['week2'])), data['week2'])
    plt.show()

if __name__ == "__main__":
    run()