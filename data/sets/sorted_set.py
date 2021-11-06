def observed():
    observations = []
    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations

def remove_observations(observations):
    is_running = True
    while(is_running):
        print("Do you wish to remove observation, y/n?")

# additional functionality to check if list is empty within loop
        if input() == "y" | input() == "yes" & len(observations) != 0:
            print("Please enter observation you wish to remove:")
            observations.remove(input())
        else:
             is_running = False

def run():
    robo_city = observed()
    remove_observations(robo_city)

    set1 = set()
    for each_value in robo_city:
        sets_tuple = (each_value, robo_city.count(each_value))
        set1.add(sets_tuple)
    set2 = sorted(set1)
    for each_tuple in set2:
        print(f"{each_tuple[0]} observed {each_tuple[1]} times.")


if __name__ == "__main__":
    run()
