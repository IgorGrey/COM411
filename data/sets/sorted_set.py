def observed():
    observations = []
    for count in range(5):
        print("Enter your observation object:")
        observations.append(input())
    return observations

def remove_observations(obsv_list):
    print("DO you wish to remove any observation from the list y/n?")
    while input() == "y":
        print("Enter the obervation you want to remove?")