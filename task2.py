import matplotlib.pyplot as plt
import numpy as np
def hyper(x_min,x_max,N):
    if x_min < x_max:
        if (x_min < 0) and (x_max > 0):
            polN = int(N/2)
            x1 = np.linspace(x_min, -0.01, polN)
            x2 = np.linspace(0.01, x_max, polN)
            y1 = 1/x1
            plt.plot(x1,y1, color= 'k')
            y2 = 1/x2
            plt.plot(x2,y2, color = 'k')
        elif (x_min >= 0) and (x_max != 0):
            if x_min != 0:
                x = np.linspace(x_min, x_max, N)
                y = 1/x
                plt.plot(x,y, color= 'k')
            else:
                x = np.linspace(0.01, x_max, N)
                y = 1/x
                plt.plot(x,y, color= 'k')
        elif (x_max <= 0) and (x_min != 0):
            if x_max != 0:
                x = np.linspace(x_min, x_max, N)
                y = 1/x
                plt.plot(x,y, color= 'k')
            else:
                x = np.linspace(x_min, -0.01, N)
                y = 1/x
                plt.plot(x,y, color= 'k')
        elif (x_max == 0) and (x_min == 0):
            print('Недопустимое значение')
        	
        plt.title('Гипербола')
    else:
        print('Недопустимое значение')




x_min = int(input('Введите X минимальное ->  '))
x_max = int(input('Введите X максимальное ->  '))
N = int(input('Введите количество точек ->  '))



hyper(x_min,x_max,N)
plt.savefig('fig_2.png')


