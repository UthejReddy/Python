#multiple line graph

#import libraries
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x=[4,5,8,9]
y=[8,4,6,7]

x2=[7,9,4,6]
y2=[4,6,4,8]

plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)

plt.title('Epic info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()

plt.grid(True,color='k')

plt.show()
