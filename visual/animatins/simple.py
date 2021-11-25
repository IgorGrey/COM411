import matplotlib as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):

    global ax
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.plot(frame, frame)
    return


def run():
    global ax
    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=500)
    plt.show()


if __name__ == "__main__":
    run()
