# coding=utf-8

import matplotlib
#matplotlib.use('WX')
#matplotlib.rcParams['backend'] = 'WX'

matplotlib.rcParams['backend'] = 'TkAgg'
import matplotlib.pyplot as plt
import csv
import math
# matplotlib.use('TkAgg')

import numpy as np
import pandas as pd     #导入pandas包
matplotlib.axes.Axes.pie
matplotlib.pyplot.pie

#pandas有个方法可以读取csv文件,read_csv
data = pd.read_csv(open("b.csv"))
#将data转换为numpy,numpy针对数值型数据
data1 = np.array(data)

#DataFrame的作用，取出data1的第7，11，14列
# t1 = pd.DataFrame(data1[:,[7,11,14]])
# print t1

def other1():
    #直接用groupby分组后续没办法处理
   # df = t1.groupby(["销售日期", "商品类型"])
   # print(df["销售金额"].sum())
   #i和j都是按照销售日期分组后的元素
   df = pd.DataFrame(
       pd.Series([i, j[j['商品类型'] == "生鲜"].shape[0], j[j['商品类型'] == "一般商品"].shape[0]]) for i, j in
       data.groupby('销售日期'))
   #columns是df的一个属性
   df.columns = ['time', 'shengxian', 'yibanshangpin']
   Ndict = df.to_dict('records')
   print(Ndict)
   length = len(Ndict)
   sum1 = []
   sum2 = []
   sum3 = []
   for i in range(length):

       data3 = int(Ndict[i]["shengxian"])
       data4 = int(Ndict[i]["yibanshangpin"])
       data5 = int(Ndict[i]["time"])
       sum1.append(data3)
       sum2.append(data4)
       sum3.append(data5)
   print (sum1)
   print (sum2)
   print (sum3)
   #绘图
   plt.plot(sum3,sum1,c = 'blue')
   plt.plot(sum3,sum2,c = 'red')
   #设置网格
   plt.grid(alpha = 0.3)
   linestyle = "--"
   color = 'r'
   #设置标题
   plt.title("Picture",fontsize = 24)
   # plt.ylabel('',fontsize = 16)
   plt.tick_params(axis= 'both',which = 'major',labelsize = 16)
   plt.savefig("a.png")
   plt.show()

def other2():

   df = pd.DataFrame(
       pd.Series([i, j[j['大类编码'] == "10"].shape[0], j[j['大类编码'] == "11"].shape[0],j[j['大类编码'] == "12"].shape[0],j[j['大类编码'] == "13"].shape[0]
                     ,j[j['大类编码'] == "14"].shape[0],j[j['大类编码'] == "15"].shape[0],j[j['大类编码'] == "20"].shape[0],j[j['大类编码'] == "21"].shape[0]
                  ,j[j['大类编码'] == "22"].shape[0],j[j['大类编码'] == "23"].shape[0],j[j['大类编码'] == "30"].shape[0],j[j['大类编码'] == "31"].shape[0]
                  ,j[j['大类编码'] == "32"].shape[0],j[j['大类编码'] == "33"].shape[0],j[j['大类编码'] == "34"].shape[0]]) for i, j in
       data.groupby('销售月份'))
   df.columns = ['time','10','11','12','13','14','15','20','21','22','23','30','31','32','33','34']
   Ndict = df.to_dict('records')
   print(Ndict)
   length = len(Ndict)
   sum1 = []
   sum2 = []
   sum3 = []
   sum4 = []
   sum5 = []
   sum6 = []
   sum7 = []
   sum8 =[]
   sum9 = []
   sum10 = []
   sum11 = []
   sum12 =[]
   sum13 = []
   sum14 = []
   sum15 = []
   for i in range(length):
       data3 = int(Ndict[i]["10"])
       data4 = int(Ndict[i]["11"])
       data5 = int(Ndict[i]["12"])
       data6 = int(Ndict[i]["13"])
       data7 = int(Ndict[i]["14"])
       data8 = int(Ndict[i]["15"])
       data9 = int(Ndict[i]["20"])
       data10 = int(Ndict[i]["21"])
       data11 = int(Ndict[i]["22"])
       data12 = int(Ndict[i]["23"])
       data13 = int(Ndict[i]["30"])
       data14 = int(Ndict[i]["31"])
       data15 = int(Ndict[i]["32"])
       data16 = int(Ndict[i]["33"])
       data17 = int(Ndict[i]["34"])
       sum1.append(data3)
       sum2.append(data4)
       sum3.append(data5)
       sum4.append(data6)
       sum5.append(data7)
       sum6.append(data8)
       sum7.append(data9)
       sum8.append(data10)
       sum9.append(data11)
       sum10.append(data12)
       sum11.append(data13)
       sum12.append(data14)
       sum13.append(data15)
       sum14.append(data16)
       sum15.append(data17)
   print (sum1)
   print (sum2)
   print (sum3)
   #绘图
   plt.plot(sum3,sum1,c = 'blue')
   plt.plot(sum3,sum2,c = 'red')

   plt.grid(alpha = 0.3)
   linestyle = "--"
   color = 'r'
   #设置x轴刻度
   plt.title("Picture",fontsize = 24)
   # plt.ylabel('',fontsize = 16)
   plt.tick_params(axis= 'both',which = 'major',labelsize = 16)
   plt.savefig("a.png")
   plt.show()

other1()



def other3():
    sum01 = []
    sum02 = []
    data2 = data1[:, [7,14,16]]
    print (data2)
    # sum3 = data2[:,[1]]
    # print(sum3)
    for list1 in data2:
        if list1[0] >= 20150101 and list1[0] <20150108:
            if list1[2] == '是':
                sum01.append(list1[1])
            else :
                sum02.append(list1[1])
        elif list1[0] >= 20150108 and list1[0] <20150115:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150115 and list1[0] <20150122:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif  list1[0] >= 20150122 and list1[0] <20150129:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150129 and list1[0] < 20150205:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150205 and list1[0] < 20150212:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 201502012 and list1[0] < 20150219:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 201502019 and list1[0] < 20150226:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        if list1[0] >= 20150226 and list1[0] < 20150305:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150305 and list1[0] < 20150312:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150312 and list1[0] < 20150319:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150319 and list1[0] < 20150326:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150326 and list1[0] < 201500402:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150402 and list1[0] < 20150409:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150409 and list1[0] < 20150416:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150416 and list1[0] < 20150423:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        elif list1[0] >= 20150423 and list1[0] < 20150430:
            if list1[2] == '是':
                sum01.append(list1[1])
            else:
                sum02.append(list1[1])
        else:
            continue
    print(sum01)
    print(sum02)
    sumyes = []
    sumno =[]
    t = 0
    for i in sum01:
        if t < len(sum01)-1 :
            print(i)
            a = (sum01[t+1] - i)/i
            sumyes.append(a)
            t = t+1
    for i in sum02:
        print(i)
        if t < len(sum02)-1:
            print(i)
            if i == 0:
                a = 0;
            else:
                a = (sum02[t+1] - i)/i
            sumno.append(a)
            t = t+1
    print(sumyes)
    print(sumno)
    #绘图
    labels = [20150101, 20150102, 20150103, 20150104, 20150105, 20150106, 20150107, 20150108, 20150109, 20150110, 20150111, 20150112, 20150113, 20150114, 20150115, 20150116, 20150117, 20150118, 20150119, 20150120, 20150121, 20150122, 20150123, 20150124, 20150125, 20150126, 20150127, 20150128, 20150129, 20150130, 20150131, 20150201, 20150202, 20150203, 20150204, 20150205, 20150206, 20150207, 20150208, 20150209, 20150210, 20150211, 20150212, 20150213, 20150215, 20150216, 20150217, 20150218, 20150219, 20150220, 20150221, 20150222, 20150223, 20150224, 20150225, 20150226, 20150227, 20150228, 20150229, 20150301, 20150302, 20150303, 20150304, 20150305, 20150306, 20150307, 20150308, 20150309, 20150310, 20150311, 20150312, 20150313, 20150314, 20150315, 20150316, 20150317, 20150318, 20150319, 20150320, 20150321, 20150322, 20150323, 20150324, 20150325, 20150326, 20150327, 20150328, 20150329, 20150330, 20150401, 20150402, 20150403, 20150404, 20150405, 20150406, 20150407, 20150408, 20150410, 20150411, 20150412, 20150413, 20150414, 20150415, 20150417, 20150418, 20150419, 20150420, 20150421, 20150422, 20150423, 20150424, 20150425, 20150426, 20150427, 20150428, 20150429, 20150430]
    men_means = sumyes
    print(len(men_means))
    women_means = sumno
    print(len(women_means))
    plt.ylim(-3, 30)
    plt.barh(range(len(women_means)), women_means)
    plt.show()


other3()


