import matplotlib.pyplot as plt
x = [1, 5, 5, 1, 1]
y = [5, 5, 1, 1, 5]
	
plt.plot(x, y, color='k', marker='o', ms=15)
plt.axis('equal')
plt.savefig('fig_1.png')
