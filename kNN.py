# coding=utf-8
import numpy
import operator
from numpy import *
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','B','C','D']
    return group,labels

def classify0(intX,dataSet,labels, k):
    dataSetSize = dataSet.shape[0]
    print (dataSetSize)
    #计算距离
    #tile是将原矩阵横向纵向的复制
    diffMat = tile(intX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat **2
    sqDistances = sqDiffMat.sum(axis = 1 )
    distances = sqDistances ** 0.5
    #选择距离最小的点
    sortedDistIndicies  = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) +1
    #排序
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
#数据标准化函数
def autoNorm(dataSet) :
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet / tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.1

group,labels = createDataSet()
result = classify0([0,0], group, labels, 3)
print(result)