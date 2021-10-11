#Ask user if he is tired
print("Are you tired?")
tired = input()

# determine level of tiredness if any
if tired == "yes" or tired == "yeah" or tired == "y":
    print("How tired are you?")
    how_tired = input()

    if how_tired == "very":
        print("You should better go sleep now")
    elif how_tired == "a little bit":
        print("A quick nap will help")
else:
    print("You should probably go to work or study")