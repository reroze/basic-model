import numpy as np

#test=np.load('./data/ix2word.npy')
#print(test)
data=[]
datanum=0
yuansunum=0

def find_max(a,yuansu):
    b=0.0
    for i in range(len(a)):
        if(a[i][yuansu]>b):
            b=a[i][yuansu]
    return b


def find_min(a,yuansu):
    b=1000.0
    for i in range(len(a)):
        if(a[i][yuansu]<b):
            b=a[i][yuansu]
    return b

with open('./数据.data','r') as f:
    line = f.readline().strip()
    while line:
        linestr=line.split()
        #print(linestr)
        line=f.readline().strip()
        data=data+[linestr]

#for i in range(len(linestr)):
    #print(linestr[i],end=" ")

#print(data)
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j]=float(data[i][j])

datanum=len(data)
yuansunum=len(data[0])

#print(data)
print(datanum)#506个样本
print(yuansunum)#14维数据
a=data.copy()
a_max=[0.0 for i in range(14)]
a_min=[0.0 for i in range(14)]
for i in range(14):
    a_max[i]=find_max(a,i)
    a_min[i]=find_min(a,i)
print(a_max)
print(a_min)
for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j]=(a[i][j]-a_min[j])/(a_max[j]-a_min[j])
print(a)
