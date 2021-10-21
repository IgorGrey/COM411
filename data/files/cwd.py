def cwd ():
# check our current working directory
    import os

    path = os.getcwd()
    print(f"The current Working Directory: {path}")
# display the content of this directory
    for file in os.listdir(path):
        print(file)

def run():
    print("Processing...")
    cwd()

if __name__ == "__main__":
  run()