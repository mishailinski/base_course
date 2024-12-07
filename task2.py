import matplotlib.pyplot as plt
import numpy as np
nul = 0
def hyper(x_min,x_max,N):
    x1 = np.linspace(-10, -0.01, 100)
    x2 = np.linspace(0.01, 10, 100)
    y = 1/x1
    plt.plot(x1,y)
    y = 1/x2
    plt.plot(x2,y)

x_min = int(-10)
x_max = int(10)
N = int(100)
polN = N/2

hyper(x_min,x_max,N)
plt.savefig('fig_2.png')


