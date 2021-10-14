print("Program Started!")
print("Please enter an ASCII code:")
code = abs(int(input()))

if code in range(32, 126):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}.")
else:
    print("Error!")

print("Program Ended!")