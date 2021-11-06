def observed():
    observations = []

    for count in range(7):
        print("Enter object observed:")
        observations.append(input())

    return observations


def run():
    print("Counting observation...")
    returned_observations = observed()

    set1 = set()
    for each_value in returned_observations:
        data = (each_value, returned_observations.count(each_value))
        set1.add(data)

    for smthelse in set1:
        print(f"{smthelse[0]} observed {smthelse[1]} times.")


if __name__ == "__main__":
    run()
