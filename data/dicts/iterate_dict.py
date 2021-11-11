def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences

def dispay_keys(data):
    print("Keys:")
    for key in data:
        print(key)
    print()
def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)
    print()
def display_items(data):
    print("Pairs:")
    for key,value in data.items():
        print(f"{key}: {value}")
    print()
def run():
    print(pattern())
    print()
    data = pattern()
    dispay_keys(data)
    display_values(data)
    display_items(data)

if __name__ == "__main__":
    run()