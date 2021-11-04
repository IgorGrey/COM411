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
    print(set1)

if __name__ == "__main__":
    run()