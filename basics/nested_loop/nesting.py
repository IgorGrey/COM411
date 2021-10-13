print("Please enter a sequence:")
sequence = input()

print("Please enter the character for the marker:")
marker = input()

marker1 = -1
marker2 = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if letter == marker:
        if (marker1 == -1):
            marker1 = position
        else:
            marker2 = position

# Display result
print(f"The distance between the markers is {marker2 - marker1 - 1}.")