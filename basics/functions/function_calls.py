def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)


def display_lower_case(word):
    print(word.lower())


def display_upper_case(word):
    print(word.upper())


def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")


def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        # even repetition
        if (repetition % 2 == 0):
            print(display_lower_case(word))
        # odd repetition
        else:
            print(display_upper_case(word))


def run():
    print("Please enter a word:")
    word = input()

    # get the user's selection
    print("What would you like to do with this word?")
    print("[1] Display in a box")
    print("[2] Display lower-case")
    print("[3] Display upper-case")
    print("[4] Display mirrored")
    print("[5] Display repeated")
    print("[6] Quit")

    response = int(input())

    # determine and execute action
    if response == 1:
        display_box(word)
    elif response == 2:
        display_lower_case(word)
    elif response == 3:
        display_upper_case(word)
    elif response == 4:
        display_mirrored(word)
    elif response == 5:
        display_repeated(word)
    else:
        print("Unknown option.")


run()