import matplotlib.pyplot as plt

slices = [4,6,3,9]
activities = ['eating','sleeping','drinking','working']
cols = ['r','k','m','c']

plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0.1,0,0))
plt.title("PIE")
plt.show()
