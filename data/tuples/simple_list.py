def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)

def run():
    chance = likelihood()
    print(f"Minimum likelihood of falling: {chance}%")

if __name__ == "__main__":
    run()