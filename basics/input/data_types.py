# Ask user to enter their name
print("What is your name human?")
name = str(input())
# Ask user to enter their age
print("How old are you?")
age = int(input())
# Ask user to enter their height in meters
print("How tall are you? (m)")
height = float(input())
# Ask user to enter their weigh in kilograms
print("How much do you weigh? (kg)")
weight = float(input())
# Bmi calculation (weight divided on height squared)
bmi = weight / height ** 2
# Show user personalised message with bmi index
print(f"{name}, your bmi index is {bmi}")