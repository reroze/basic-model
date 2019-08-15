#coding:utf-8
import numpy as np
import random
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

def loadDataSet():
    dataMat=[]
    labelMat=[]
    fr=open('testSet.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    fr.close()
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))


def gradAscent(dataMatIn, classLabels):
    dataMatrix=np.mat(dataMatIn)
    labelMat=np.mat(classLabels).transpose()
    m, n=np.shape(dataMatrix)
    alpha=0.01
    maxCycles=500
    weights=np.ones((n,1))
    weights_array=np.array([])
    for k in range(maxCycles):
        h=sigmoid(dataMatrix*weights)
        error=labelMat-h
        weights=weights+alpha*dataMatrix.transpose()*error#x*(y-y~) 由于是梯度上升所以用+号 每一次都整体训练和优化
        weights_array=np.append(weights_array,weights)
    weights_array=weights_array.reshape(maxCycles,n)
    return weights.getA(), weights_array#gatA()表示取回数组形态


def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n=np.shape(dataMatrix)
    weights=np.ones(n)
    weights_array=np.array([])
    for j in range(numIter):
        dataIndex=list(range(m))
        for i in range(m):
            alpha=4/(1.0+j+i)+0.01
            randIndex=int(random.uniform(0,len(dataIndex)))
            h=sigmoid(sum(dataMatrix[randIndex]*weights))
            error=classLabels[randIndex]-h
            weights=weights+alpha*error*dataMatrix[randIndex]
            weights_array=np.append(weights_array,weights, axis=0)
            del(dataIndex[randIndex])
    weights_array=weights_array.reshape(numIter*m,n)
    return weights, weights_array


def plotBestFit(weights):
    dataMat, labelMat = loadDataSet()
    dataArr=np.array(dataMat)
    n =np.shape(dataMat)[0]
    xcord1=[]; ycord1=[]
    xcord2=[]; ycord2=[]
    for i in range(n):
        if int(labelMat[i]) ==1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig =plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=20,c='red', marker='s',alpha=.5)
    ax.scatter(xcord2, ycord2, s=20,c='green',alpha=.5)
    x=np.arange(-3.0,3.0,0.1)
    y=(-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.title('bestFit')
    plt.xlabel('X1')
    plt.ylabel('x2')
    plt.show()


dataMat, labelMat=loadDataSet()
weights1,weights_array1=stocGradAscent1(np.array(dataMat),labelMat)

weights2,weights_array2=gradAscent(dataMat,labelMat)
#plotBestFit(weights1)
plotBestFit(weights2)