#Get number of cables to evoid from user
print("How many live cables must I avoid?")
evoid_cables = int(input())

cables_count = 0

#Go through each cable until desired numeber reached
while cables_count < evoid_cables:
    print("Avoiding...", end= "")
    print(f"...Done! {cables_count} live cables avoided!")
    cables_count = cables_count + 1

print()
print(f"...Done! {evoid_cables} live cable avoided!")