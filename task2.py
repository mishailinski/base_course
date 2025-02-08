import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2 * np.pi, 100)


fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
circle = plt.plot([],[])

def update(frame):
    r = alpha * t[frame]
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    circle.set_data(x, y)
    return circle

ani = FuncAnimation(fig, update, frames=len(t))
ani.save('animation_3.gif', writer="pillow")