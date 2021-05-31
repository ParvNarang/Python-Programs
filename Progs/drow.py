import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

#population = [21,45,23,67,32,78,27,78,56,90,12,324,342,554,32,12,35,667]
#bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]
#x = [1,2,6]
#y = [1,2,8]
#x1 = [0,5,6]
#y1 = [4,3,8]


#plt.plot(x,y,'g',label="Line 1",linewidth=2)
#plt.plot(x1,y1,'c',label="Line 2",linewidth=2)
#plt.bar(x,y,label="PART1")
#plt.bar(x1,y1,label="PART2")
#plt.hist(population,bins, histtype='bar' ,rwidth=0.7,color='g')
#plt.scatter(x,y,label="POINTS")
#plt.subplot(211)
#plt.plot(x1,y1)

#plt.subplot(212)
#plt.plot(x,y)

plt.legend()
plt.title("GRAPH")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
