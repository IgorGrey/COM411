#Ask user what type of advanture would it be
print("What type of adventure should I have?")
advanture = input()

#determite what pass it would it be
if advanture == "short" or advanture == "long":
    print("Taking the safe route!")

elif advanture == "short" or advanture == "scary":
        print("Entering the dark forest!")
else:
    print("Not sure which route to take.")