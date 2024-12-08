import matplotlib.pyplot as plt
import numpy as np
def ellips(x_min,x_max,N):
       x = np.linspace(x_min, x_max, N)
       y = abs((1-(x**2-a**2))*b**2)**0.5
       plt.plot(x,y, color= 'k')
a = 2
b = 4
ellips(-10,10,100)
plt.savefig('fig_3.png')