##Area plot

##import libraries
from matplotlib import pyplot as plt

##create sample lists
days=[1,2,3,4,5]

sleeping=[4,5,6,12,7]
eating=[4,8,8,7,3]
working=[3,2,1,4,5]
playing=[8,7,9,5,6]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='g',label='eating',linewidth=5)
plt.plot([],[],color='k',label='working',linewidth=5)
plt.plot([],[],color='r',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,color=['m','g','k','r'])

plt.title('area plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
plt.show() 
