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

import re

line = "this hdr-biz model ser args= server"
patt = r'serverorf'
pattern = re.compile(patt)
result = pattern.findall(line)
print(result)

import xlwt
xls = xlwt.Workbook()
# 设置字体格式
Font0 = xlwt.Font()
Font0.name = "Times New Roman"
Font0.colour_index = 2
style0 = xlwt.XFStyle()
# 实例化一个工作表，名叫Sheet1
sht1 = xls.add_sheet('Sheet1')
a = 0
sht1.write(a, 1, 'p', style0)
xls.save('./mydata.xls')

#生成2维数组，20000个长度为100的数组
finaldata = [ [0] * 100 for i in range(20000)]
print(finaldata)

#写入遇到超过256列无法写入的情况
#考虑用分表
# !/usr/bin/python
# -*- coding:utf8 -*-

import xlwt

def write_data_to_excel():
    print('开始生成')
    wbk = xlwt.Workbook()
    sheets = []
    sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
    sheets.append(sheet)
    for i in range(500):
        print('正在生成：第' + str(i + 1) + '条数据 . . .')
        for j in range(769):
            # 计算第几个表
            scount = j / 256
            # 如果表的个数少于该有的个数，则新建
            if (len(sheets) <= scount):
                sheets.append(wbk.add_sheet('Sheet' + str(scount + 1), cell_overwrite_ok=True))
            # 计算第几列，如果是256的倍数，序号应从0开始
            col = j % 256
            sheets[scount].write(i, col, str(j))
    wbk.save('test.xls')
    print('生成成功')


if __name__ == '__main__':
    write_data_to_excel()