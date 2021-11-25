import matplotlib as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):



def run():

    global ax

    x = [2, 4, 6, 8, 10]
    y = [2, 4, 6, 8, 10]
    ax.plot(x(frame), y(frame))

    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=100)
    plt.show()

if __name__ == "__main__":
    run()