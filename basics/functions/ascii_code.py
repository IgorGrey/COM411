print("Program Started!")

print("Please enter a standard character:")
char = input()

if len(char) != 1:
    print("Program Ended!")
else:
    value = ord(char)
    print(f"The ASCII code for {char} is {value}.")