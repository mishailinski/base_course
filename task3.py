import numpy as np
import math as mh
from task1 import acceleration_of_gravity as g
x0 = 2
y0 = 1
V0x = 50
arr = np.zeros((6,3))
for t in range (1,6):
    x = x0 + V0x*t
    y = y0 + V0x*t - (g*t**2)/2
    arr[t, 0] = t
    arr[t, 1] = x
    arr[t, 2] = y
print(arr)





