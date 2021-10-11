#Ask user How many cables should I remove?
print("How many cables should I remove?")
cables_removed = int(input())

# Declare a variable to count the current number of cables removed
iterations = 0

# Display ready message
print("Starting removing cables...")

# Display the current count
while iterations < cables_removed:
    # Update the current iteration count
    iterations = iterations + 1
    print("Cable removed")

# Display completion message
print()
print(f"In total {cables_removed} cabel have been removed !")

