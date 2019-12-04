import numpy as np
"""关于numpy的一些测试"""
t1 = np.array([1,2,3])
print(t1.reshape(3,1))
#t/0会出现inf
print(t1/0)

t2 = np.array(range(24)).reshape(4,6)
print(t2)
##arrange是numpy的内置函数，能直接生成数组
t3 = np.array(range(24)).reshape(4,6)
print(t3)
#vstack是竖直拼接
t4 = np.vstack((t3,t2))
print(t4)
#hstack是水平拼接
t5 = np.hstack((t3,t2))
print(t5)

