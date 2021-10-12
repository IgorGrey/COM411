print("What strange markings do you see?")
markings = input()

for index in range(0, len(markings), 1):
    print(f"Index {index}: ",end="")
    print(markings[index])