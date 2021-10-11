#Ask user what sound was heard
print("What did I hear?")
heard = input()

#Ask user what was seen
print("What did I see?")
seen = input()

#Determine what path to take
if heard == "grrr" and seen == "two red eyes":
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")