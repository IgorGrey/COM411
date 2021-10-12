# Ask user to enter how many numbers should be added
print("How many numbers should I sum up?")
amount = int(input())

# Create variables needed to calculation
number = 1
sum = 0

# A while loop to repeatedly prompt the user for a number.
# The specified number should be added to a running total.
while number <= amount:
    print(f"Please enter your number {number} of {amount}:")
    user_number = int(input())
    sum = user_number + user_number
    number = number + 1

#Show results
print(f"The answer is {sum}.")