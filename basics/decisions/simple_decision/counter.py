#Please enter the first whole number and show the number to user
print("Please enter the first whole number.")
first_number = int(input())
print(f"You selected {first_number} as your first number")
#Please enter the second whole number and show the number to user
print("Please enter the second whole number.")
second_number = int(input())
print(f"You selected {second_number} as your first number")
#Please enter the third whole number and show the number to user
print("Please enter the third whole number.")
third_number = int(input())
print(f"You selected {third_number} as your first number")

odd = 0
even = 0

if first_number % 2 == 0:
    even += 1
else:
    odd += 1

if second_number % 2 ==0:
    even += 1
else:
    odd += 1

if third_number % 2 ==0:
    even += 1#
else:
    odd += 1

print(f"There were {odd} even and {even} odd numbers.")