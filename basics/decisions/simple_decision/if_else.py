#Ask user what activity Beep should perform
print("Please enter the activity to be performed.")
activity = input()
# check if activity is calculation
if activity == "calculate":
    print("Performing calculations...")
# If it is not, perform any other avtivity
else: print("Performing activity...")
# indicate that activities completed
print("Activity completed!")