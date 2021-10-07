#ask user to enter number
print("Please enter a whole number.")
number = int(input())
# check if number can be devided on 2 without left over and print the result with corresponding message
if number % 2 == 0:
    print(f"The number {number} is an whole number.")
else: print(f"The {number} is an odd number.")