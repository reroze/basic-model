#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import random as rd
#生成一个100000个数的2*2的方格
X_list=[0.0 for i in range(100000)]
Y_list=[0.0 for i in range(100000)]
Label=[0 for i in range(100000)]

for i in range(100000):
    X_list[i]=rd.uniform(0,2)
    Y_list[i]=rd.uniform(0,2)

for i in range(100000):
    if(X_list[i]<1.0 and Y_list[i]<1.0):
        Label[i]=-1
        #plt.scatter(X_list[i],Y_list[i],s=1,color='blue')
    if(X_list[i]>=1.0 and Y_list[i]>=1.0):
        Label[i]=-1
        #plt.scatter(X_list[i], Y_list[i],s=1, color='blue')
    if (X_list[i] < 1.0 and Y_list[i] >= 1.0):
        Label[i]=1
        #plt.scatter(X_list[i], Y_list[i],s=1, color='red')
    if (X_list[i] >= 1.0 and Y_list[i] < 1.0):
        Label[i]=1
        #plt.scatter(X_list[i], Y_list[i],s=1, color='red')
    #print(i)
