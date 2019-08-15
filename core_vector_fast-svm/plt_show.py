#coding:utf-8
import data_create
import matplotlib.pyplot as plt
Color=[]
X_list=data_create.X_list
Y_list=data_create.Y_list
for i in range(100000):
    if (X_list[i] < 1.0 and Y_list[i] < 1.0):
        Color.append('blue')
    if (X_list[i] >= 1.0 and Y_list[i] >= 1.0):
        Color.append('blue')
    if (X_list[i] >= 1.0 and Y_list[i] < 1.0):
        Color.append('red')
    if (X_list[i] < 1.0 and Y_list[i] >= 1.0):
        Color.append('red')

#print(Color)
#print(len(Color))
plt.scatter(X_list,Y_list,s=1,c=Color)

#plt.scatter(X_list[0],Y_list[0],s=1,color='red')
#plt.plot(X_list[0],Y_list[0],color='red')
plt.xlim((0,2))
plt.ylim((0,2))
plt.xlabel("x'slabel")
plt.ylabel("y's;abel")
plt.show()