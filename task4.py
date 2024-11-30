import numpy as np
import math as mh
N = int(input())
M = int(input())
trigonometry_array = np.zeros((N, M))
for i in range(0,N):
    for j in range(0,M):
        a = mh.sin(N*i + M*j + 1)
        if a >= 0:
            trigonometry_array[i][j] = a
        else:
            trigonometry_array[i][j] = 0
print(trigonometry_array)
