import numpy as np
import math as mh
from task1 import acceleration_of_gravity as g
x0 = int(input())
y0 = int(input())
V0x = int(input())
arr = np.zeros((6,3))
for t in range (1,6):
    x = x0 + V0x*t
    y = y0 + V0x*t - (g*t**2)/2
    arr[t, 0] = t
    arr[t, 1] = x
    arr[t, 2] = y
print(arr)





