import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, (ax1, ax2, ax3) = plt.subplots(
    nrows=3
    
)

plt.suptitle("Sensor Output")

def animate(i):
    '''
    This function animates the plots so live data from the sensor
    can be displayed
    '''
    times = []
    dists = []
    loads = []
    # read data
    with open('out.txt', 'r') as lines:
        for line in lines:
            tim, dist, load = line.split(",")
            times.append(float(tim))
            dists.append(float(dist))
            loads.append(float(load))

    # update plots
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax1.set_title("Distance vs Time")
    ax2.set_title("Load vs Time")
    ax3.set_title("Distance vs Load")
    ax1.plot(times[-10:], dists[-10:])
    ax2.plot(times[-10:], loads[-10:])
    ax3.plot(loads[-10:], dists[-10:])


ani = FuncAnimation(fig, animate, interval=1000)

fig.tight_layout()

plt.show()
