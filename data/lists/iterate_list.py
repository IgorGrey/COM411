def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    dir =  directions()
    for index in range(len(dir)):
        print(f"{index}: {dir[index]}")

def run():
    menu()

if __name__ == "__main__":
    run()