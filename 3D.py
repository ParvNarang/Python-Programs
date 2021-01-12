from mpl_toolkits.mplot3d import axis3d
import matplotlib.pyplot as plt
import random

while True:
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection="3d")
    x = [random.randint(2, 1000), random.randint(2, 1000), random.randint(2, 1000), random.randint(2, 1000)]
    y = [random.randint(2, 1000), random.randint(2, 1000), random.randint(2, 1000), random.randint(2, 1000)]
    z = [random.randint(2, 1000), random.randint(2, 1000), random.randint(2, 1000), random.randint(2, 1000)]

    ax1.plot(x, y, z)
    plt.show()