import numpy as np
import math
from task1 import acceleration_of_gravity as g
from task1 import euler_number as eu
from task1 import boltzmann_const as k
from task1 import planks_const as n 
from task1 import pi
h = 100
T = 200
e = 300
a = math.radians(45)
B = math.radians(35)
tan_a = math.tan(a)
tan_B = math.tan(B)
cos_a = math.cos(a)
v = ((g*h*tan_B**2)/(2*cos_a**2*(1-tan_B*tan_a)))
print(v)
N = (2/pi**0.5)*(h/(k*T)**3/2)*(eu**(-e/k*T))*e**(T/2)
print(N)