"""数据可视化操作"""
#pyplot中的基础绘图语法
import numpy as np
import matplotlib.pyplot as plt
data = np.arange(0,1,0.01)
plt.title('lines') #添加标题
plt.xlabel('x') #添加x轴的名称
plt.ylabel('y') #添加y轴的名称
plt.xlim((0,1)) #确定x轴的范围
plt.ylim((0,1)) #确定y轴的范围
#设置x轴和y轴的刻度
plt.xticks([0,0.2,0.4,0.6,0.8,1.0])
plt.yticks([0,0.2,0.4,0.6,0.8,1.0])
plt.plot(data,data**2)
plt.plot(data,data**4)
#添加图例
plt.legend(['y=x^2','y=x^4'])
plt.savefig('../tmp/y=x^2.png')
plt.show()

#包含子图绘制的基础语法
rad = np.arange(0,np.pi*2,0.01)
#第一幅子图
p1 = plt.figure(figsize=(8,6),dpi=80)
#创建一个2行1列的子图，并开始绘制第一幅
ax1 = p1.add_subplot(2,1,1)
plt.title('lines')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0,1))
plt.ylim((0,1))
plt.xticks([0,0.2,0.4,0.6,0.8,1.0])
plt.yticks([0,0.2,0.4,0.6,0.8,1.0])
plt.plot(rad,rad**2)
plt.plot(rad,rad**4)
plt.legend(['y=x^2','y=x^4'])
#第二幅子图
#开始绘制第二幅
ax2 = p1.add_subplot(2,1,2)
plt.title('sin/cos')
plt.xlabel('rad')
plt.ylabel('value')
plt.xlim((0,np.pi*2))
plt.ylim((-1,1))
plt.xticks([0,np.pi/2,np.pi,np.pi*1.5,np.pi*2])
plt.yticks([-1,-0.5,0,0.5,1])
plt.plot(rad,np.sin(rad))
plt.plot(rad,np.cos(rad))
plt.savefig('../tmpsincos.png')
plt.show()
