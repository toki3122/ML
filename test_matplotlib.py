#matplotlib is the numerical mathematical extension for numpy and is a plotting library
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10)
y=np.arange(2,12)
#plt.scatter(x,y,c='g')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('2D graph')
#plt.show()
#plt.plot(x,x*x,'o-')
#plt.show()
# plt.subplot(2,2,1)
# plt.plot(x,x,'r')
# plt.subplot(2,2,2)
# plt.plot(x,x*x,'g')
# plt.subplot(2,2,3)
# plt.plot(x,x*x*x,'b')
# plt.subplot(2,2,4)
# plt.plot(x,x*x*x*x,'c')
# plt.show()
x=np.arange(0,4*np.pi,0.001)
y=np.sin(x)
# plt.plot(x,y)
# plt.show()
x=[2,8,10]
y=[1,7,9]
x1=[3,8,1]
y1=[2,7,6]
# plt.bar(x,y,align='center')
# plt.bar(x1,y1,color='g')
# plt.show()
a=np.array([1,2,3,4,5,6,7,7,8,8,9,9,9,0,0,0,0,0])
# plt.hist(a)
# plt.show()
data=[np.random.normal(0,std,100) for std in range(1,4)]
# plt.boxplot(data,vert=True,patch_artist=True)
# plt.show()
labels='python','c++','ruby','java'
sizes=[215,130,245,210]
colors=['gold','yellowgreen','lightcoral','lightskyblue']
explode=(.1,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)
plt.show()