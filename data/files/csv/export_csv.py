def export(file_path, num_bots):
    print("Exporting...")
    with open(file_path, "a") as file:
        for count in range(num_bots):
            print("Please enter the bot id:")
            bot_id = int(input())

            print("Please enter the bot name:")
            bot_name = input()

            print("Please enter the bot paint:")
            bot_paint = input()

            data = f"{bot_id},{bot_name},{bot_paint}\n"
            file.write(data)
    print("Done!")


def run():
    export("exported_bots.csv", 2)


if __name__ == "__main__":
    run()
