import random
import math
import numpy as np
import pandas as pd
e = []
f = []
g = []
score  = []
for i in range(10):
    a = np.random.randint(50,100)
    e.append(a)
    b = np.random.randint(1,100)
    f.append(b)
    c = np.random.randint(60,100)
    g.append(c)
#竖直拼接
data = np.vstack((e,f,g))
#生成二维数组
data  = pd.DataFrame(data,index = list("abc"),columns =list("1234567890"),)
print(data)

def sorted():
    data1 = []
    data3 = []
    for i in range(10):
        a = np.random.randint(1,100)
        data1.append(a)
    print(data1)
    data2 = np.sort(data1)
    print(data2)
    print("请输入y")
    y = input()
    x = int(y)
    if x < data2[0]:
        fn = 0
        print(fn)
    elif x > data2[-1]:
        fn = 1
        print(fn)
    else:
        for k in range(len(data1)):
            if x > data2[k] and x < data2[k+1]:
                fn = k/len(data2)
                data3.append(fn)
                k += 1
            else:
                continue
    print(data3)
sorted()