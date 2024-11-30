import task4
from task4 import trigonometry_array
from task4 import N
a = int(input('Первый столбец '))-1
b = int(input('Второй стобец '))-1

for i in range(N):
    trigonometry_array[i,a],trigonometry_array[i,b] = trigonometry_array[i,b],trigonometry_array[i,a]
print(trigonometry_array)

        