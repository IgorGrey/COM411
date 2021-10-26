def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    movements()
    memory = movements()
    for index in range(0, len(memory), 2):
        print(f"{memory[index]} for {memory[index+1]} steps")

if __name__ == "__main__":
  run()