import matplotlib.pyplot as plt
import numpy as np
k = 1
N = int(0.1)
def rose(k,N):
    u = np.linspace(0,8*np.pi,N)
    r = np.sin(k*u)
    x = r * np.cos(u)
    y = r * np.sin(u)
    plt.plot(x,y)
        

rose(k,N)
plt.savefig('fig4_4.png')