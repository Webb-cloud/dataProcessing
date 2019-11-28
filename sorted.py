#_*_ coding:utf-8 _*_
import sys
import itertools
data = [1,2,3,4,5]
length = len(data)
print("请输入位数： ")
x = input()
sortedData = []
sortedData1 = []
for i in range(1,len(data)+1):
    iter = itertools.permutations(data,i)
    sortedData.append(list(iter))
# #打印所有可能的排列
# print(sortedData)
#取输入位数的排列
i = int(x)-1
print(sortedData[i])