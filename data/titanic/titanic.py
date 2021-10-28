import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...", end="")
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)
        for line in csv_reader:
            records.append(line)
    print("Done!")

def display_menu():
    print("""
     Please select one of the following options:
     [1] Display the names of all passengers
     [2] Display the number of passengers that survived
     [3] Display the number of passengers per gender
     [4] Display the number of passengers per age group
    """)

    return int(input())

def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

    selected_option = display_menu()
    print(f"You have selection option: {selected_option}")

if __name__ == "__main__":
    run()