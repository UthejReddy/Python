##Pie_Chart
from matplotlib import pyplot as plt
slices=[7,1,5,6]
activities=['sleeping','eating','working','playing']
cols=['c','m','g','r']

plt.pie(slices,
       labels=activities,
       colors=cols,
       startangle=90,
       explode=(0,0,0.1,0),
       autopct='%1.5f%%')
plt.title('Pie_Chart')
plt.show()