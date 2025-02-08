import matplotlib.pyplot as plt
import numpy as np


def astr(R):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)  # Параметр

    x = R * (np.cos(t))**3
    y = R * (np.sin(t))**3

    plt.plot(x, y, lw=3)
    plt.axis('equal')
    plt.savefig('astr.png')



astr(4)