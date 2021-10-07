#ask user towards which direction Beep should move paint brush
print("Towards which direction should I paint (up, down, left or right)?")
direction = input()
# check sellected direction and execute corresponding command and write relevant message
if direction == "up":
    print("I am painting in the ↑ direction!")
elif direction == "right":
    print("I am painting in the → direction!")
elif direction == "left":
    print("I am painting in the ← direction!")
elif direction == "down":
    print("I am painting in the ↓ direction!")
#indicate we done with message
else: print("Done painting")
