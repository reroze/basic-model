#coding:utf-8

def tiaojie(x):
    if(x<0):
        return 0
    if(x>1):
        return 1
    return x

def smo(a1,a2):
    iter=0
    a_1=a1
    a_2=a2
    gradient=4*a_1-2
    biao = 1.0*gradient/10
    while(iter<40):
        a_1=a_1-biao
        a_1=tiaojie(a_1)
        a_2=1-a_1
        print(biao)
        if(biao<0.01):
            iter+=1
        gradient = 4 * a_1 - 2
        biao = gradient / 10
    return a_1,a_2


a1=1
a2=0
a1,a2=smo(a1,a2)
print(a1,a2)