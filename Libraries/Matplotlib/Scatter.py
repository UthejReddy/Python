##Scatter plot
from matplotlib import pyplot as plt
x=[1,5,7,2,9,6,4,5,6,4]
y=[4,4,5,6,12,4,5,6,5,4]

plt.scatter(x,y,label='skitscat',color='k')

plt.title('scatter')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
plt.show()