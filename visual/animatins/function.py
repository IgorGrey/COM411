import matplotlib.pyplot as plt
import matplotlib.animation as animation



def animate(frame):
    print(f"Frame: {frame}")


def run():
    global fig

    fig, ax = plt.subplots()
    some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100)
    plt.show()


if __name__ == "__main__":
    run()