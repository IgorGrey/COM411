def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("...Done!")

def run():
    search("library.txt")

if __name__ == "__main__":
    run()