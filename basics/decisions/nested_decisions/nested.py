# Ask user what book type
print("What type of cover does the book have?")
book_type = input()
# If book is soft type we check if its perfect-bound or not
if book_type == "soft":
    print("Is the book perfect-bound?")
    book = input()
# appropriate message will be printed depending on previous input results
    if book == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
# If book type not soft we assume its hard cover book type and print following message
else:
    print("Books with hard covers can be more expensive!")