print("Please enter a number:")
number = int(input())
factorial = 1
i = 1

while i <= number:
    factorial = factorial * i
    i = i + 1

print()
print(f"The factorial is {factorial}.")