
##Histogram
##import libraries
from matplotlib import pyplot as plt

##List of integers
ages=[10,21,54,84,20,14,56,20,32,65,89,45,18,54,45,97]
bins=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins,histtype='bar',rwidth=0.8)

plt.title('histtogram')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
plt.show()
