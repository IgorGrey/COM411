import random

print("Please enter the minimum value:")
min_value = int(input())

print("Please enter the maximum value:")
max_value = int(input())

random_number = random.randrange(min_value, max_value)

print(f"I am thinking of a number between {min_value} and {max_value}.")
print("Can you guess what it is?")

guessed_correctly = False

while not guessed_correctly:
    print("Please enter a number:")
    guess = int(input())

    if guess == random_number:
        print("Congratulations! You guessed the correct answer!")
        guessed_correctly = True
    elif guess < random_number:
        print("Guess higher")
    else:
        print("Guess lower")

print("Game over!")