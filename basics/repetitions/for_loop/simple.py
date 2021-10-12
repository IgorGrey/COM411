# ask user how many of the ascii drawing to copy
print("How many mountains should I display?")
copies = int(input())

# use for loop to duplicate the following lines of code given number of times
for count in range(0, copies):
    print("     ___      ")
    print("    /^  \     ")
    print("   /   ^ \    ")
    print("  /  ^    \   ")
    print(" /    ^    \  ")