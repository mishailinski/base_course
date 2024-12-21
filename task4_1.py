import matplotlib.pyplot as plt
import numpy as np
k = 1
b = 0.2
N = 1000
u = np.linspace(0, 8*np.pi,N)
r = np.exp(b*u)
x = r * np.cos(u)
y = r * np.sin(u)

plt.plot(x,y)
plt.savefig('fig4_1.png')