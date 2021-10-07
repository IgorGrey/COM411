#the user to enter the first number
print("Please enter the first number.")
first_number = int(input())
#the program should then read in the user’s first number.
print(f"You selected {first_number} as your first numebr")
#user to enter the second number.
print("Please enter the second number.")
second_number = int(input())
#the program should then read in the user’s second number.
print(f"You selected {second_number} as your second numebr")
#The program should then decide which of the two numbers is the smallest and display the message
# "The first number is the smallest!" if the first number is smaller, "The second number is the smallest!"
# if the second number is smaller or "Both are equal!" if both numbers are equal in value.
print("----------------------------------------------------")
if first_number < second_number:
    print("The first number is the smallest!")
elif second_number < first_number:
    print("The second number is the smallest!")
else:
    print("Both are equal!")