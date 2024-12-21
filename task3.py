import matplotlib.pyplot as plt
import numpy as np

def ellips(x_min,x_max,N):
       m = np.linspace(0, 2*np.pi,N)
       y = a * np.cos(m)
       x = b * np.sin(m)
       plt.plot(x,y, color= 'k')
a = 2
b = 4
N = 100
plt.axis('equal')
ellips(a,b,N)
plt.savefig('fig_3.png')