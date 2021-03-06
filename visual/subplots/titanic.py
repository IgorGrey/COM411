import matplotlib.pyplot as plt
import csv

def read_data():
    with open('titanic.csv') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = {
            'survived': [],
            'sex': [],
            'age': [],
            'fare': []
        }

        for row in csv_reader:
            if not has_empty_values(row):
                data['survived'].append(float(row[1].strip()))
                data['sex'].append(row[4].strip())
                data['age'].append(float(row[5].strip()))
                data['fare'].append(round(float(row[9].strip())))

    return data

# User function designed to check for empty string list
def has_empty_values(list_to_check):
    for item in list_to_check:
        if item == "":
            return True
    return False

def run():
    data = read_data()

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(2, 2)
    ax1.plot(data)
    ax2.plot(data)
    ax3.plot(data)
    ax4.plot(data)
    plt.show()

if __name__ == "__main__":
    run()