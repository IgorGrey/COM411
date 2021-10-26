def directions():
    directions = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    dir = directions()
    for u_dir in range(len(dir)):
        print(f"{u_dir}: {dir[u_dir]}")
    u_dir = int(input())
    return dir[u_dir]

def run():
    route = []
    print("Working out escape route...")
    for number in range(0, 5, 1):  #Call the function menu and append the returned direction to the list route x5
       route.append(menu())
    print(f"Escape route: {route}")

if __name__ == "__main__":
    run()