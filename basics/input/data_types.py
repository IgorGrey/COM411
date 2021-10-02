# Ask user to enter their name
print("What is your name human?")
name = input()
# Ask user to enter their age
print("How old are you?")
age = input()
# Ask user to enter their height in meters
print("How tall are you? (m)")
height = input()
# Ask user to enter their weigh in kilograms
print("How much do you weigh? (kg)")
weight = input()
# Bmi calculation (weight divided on height squared)
bmi = weight/height**2
# Show user personalised message with bmi index
print(f"{name}, your bmi index is {bmi}")

#Traceback (most recent call last):
  File "C:\Users\maili\PycharmProjects\COM411\basics\input\data_types.py", line 14, in <module>
    bmi = weight/height*2
TypeError: unsupported operand type(s) for /: 'str' and 'str'