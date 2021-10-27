def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)

def run():
    chance = likelihood()

    print(f"Minimum likelihood of falling: {chance[0]}%")
    print(f"Minimum likelihood of falling: {chance[1]}%")

if __name__ == "__main__":
    run()