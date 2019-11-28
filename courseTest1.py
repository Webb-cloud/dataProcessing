import csv
import math
import pandas as pd
data = pd.read_csv("stud.consumption.csv",encoding= 'gbk')
print(data["平均月生活费(元)"])
data1 = data["平均月生活费(元)"]
K = 1 + math.log10(len(data))/math.log10(2)
print(K)
#将组数变为10
aclK = 10
distance = (data1.max()-data1.min())/aclK
print(distance)
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
data2 = [a,b,c,d,e,f,g,h,i,j]
for i in data1:
    if i >= data1.min() and i < data1.min()+distance:
        a.append(i)
    elif i >= data1.min() and i < data1.min()+2*distance:
        b.append(i)
    elif i >= data1.min()+2*distance and i <data1.min()+3*distance:
        c.append(i)
    elif i >= data1.min()+3*distance and i < data1.min() + 4 * distance:
        d.append(i)
    elif i >= data1.min() + 4 * distance and i < data1.min() + 5 * distance:
        e.append(i)
    elif i >= data1.min()+5*distance and i <data1.min()+6*distance:
        f.append(i)
    elif i >= data1.min()+6*distance and i < data1.min() + 7 * distance:
        g.append(i)
    elif i >= data1.min() + 7 * distance and i < data1.min() + 8* distance:
        h.append(i)
    elif i >= data1.min()+8*distance and i < data1.min() + 9* distance:
        i.append(i)
    elif i >= data1.min() + 9 * distance and i < data1.max():
        j.append(i)
    else:
        continue
print(data2)
from pandas.core.frame import DataFrame
# count1 = []
# for i in range(len(data2)):
#     pinlv = data2[i].count()
#     print(pinlv)
newdata=DataFrame(data2)
type(newdata)
print(newdata)