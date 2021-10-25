import json


def read(file_path):
    with open(file_path) as file:
        data = json.load(file)

        city_name = data["city"]
        print(f"City Name: {city_name}")

        population_size = data["population"]
        print(f"Population Size: {population_size}")

        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()

