#coding:utf-8
import random as rd
a=[0,1,0]

def tiaojie(x,T):
    if(x<0):
        return 0
    if(x>T):
        return T
    return x


def youhua(a,i1,i2,T):#将i1当做主元
    gradient=4*a[i1]-2*T
    biao=gradient/10
    a[i1]-=biao
    tiaojie(a[i1],T)
    a[i2]=T-a[i1]
    return biao


def smo(a):
    iter=0
    biao=0
    while(iter<80):
        i1=int(rd.uniform(0,len(a)))
        i2=int(rd.uniform(0,len(a)))
        while(i1==i2):
            i2=int(rd.uniform(0,len(a)))
        T=a[i1]+a[i2]
        biao=youhua(a,i1,i2,T)
        if(biao<0.01):
            iter+=1

smo(a)
print(a)