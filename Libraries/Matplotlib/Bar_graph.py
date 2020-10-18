
##Bar plot
from matplotlib import pyplot as plt
plt.bar([6,5,4,8],[4,5,6,7],label="example one")
plt.bar([8,7,3,2],[8,2,8,1],label="example two",color='g')

plt.title('Bar plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
plt.show()