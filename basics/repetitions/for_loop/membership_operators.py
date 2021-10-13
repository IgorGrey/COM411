print("What phrase do you see?")
phrase = input()

print("")
print("Reversing...")
print("The phrase is ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)