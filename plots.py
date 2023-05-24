import matplotlib.pyplot as plt

# read data
with open('./out.txt') as file:
    data = [line[0:-2].split(',') for line in file]
    times = [float(line[0]) for line in data]
    dists = [float(line[1]) for line in data]
    loads = [float(line[2]) for line in data]

# convert units and normalize data
startTime = times[0]
times = [time - startTime for time in times]

initialDeflection = dists[0]
dists = [(dist-initialDeflection) / 1000 for dist in dists]

fig, (ax1, ax2) = plt.subplots(
    nrows=2
)

# set up plots
plt.suptitle("Data")

ax1.set_title("Deflection Over Time")
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Distance [m]")

ax2.set_title("Applied Load Over Time")
ax2.set_xlabel("Time [s]")
ax2.set_ylabel("Load [N]")

ax1.plot(times, dists)
ax2.plot(times, loads)

fig.tight_layout()

plt.show()