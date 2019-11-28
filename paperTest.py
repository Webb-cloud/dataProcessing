import math
import numpy as np
# data2 = [166.44,179.15,184.34,193.17,193.81,202.44,214.48,266.22,282.37,365.52,380.08,397.23,412.56,428.31,443.23,450.01,458.25,465.64,476.26,486.39,494.9,503.96,515.92,
#         532.58,548.88,566.8,589.98,617.82,650.38,676.87,707.21,744.85,777.99,802.16]
# data1 = [223.37,241.66,258.93,262.83,263.81,263.86,275.72,277.77,287.88,301.13,310.88,320.31,313.77,303.18,296.12,290.23,287.31,285.09,280.83,280.73,283.08
#         ,286.46,294.43,307.66,326.04,351.86,390.8,422.73,452.21,464.48,473.7,476.66,461.68,442.56]
# data3 = [269.37,275.35,282.39,288.7,291.29,296.92,307.87,313.51,310.05,326.75,347.06,463.98,483.74,505.22,518.4,528.97,539.8,549.17,560.28,573.97,589.27,
#         602.99,631.65,665.74,696.82,733.7,790.7,856.17,923.28,954.34,986.87,1021.76,1045.29,1056.46]
# data = [1432.03,1469.13,1507.33,1512.49,1540.03,1569.34,1620.67,1662.58,1658.95,1729.55,1709.26,1719.43,1715.4,1710.97,1699.06,1661.16,1616.08,1551.77,
#         1499.99,1471.34,1456.3,1454.77,1468.87,1492.43,1513,1539.95,1585.16,1633.14,1683.51,1696.94,1707.37,1717.52,1714.55,1709.51]
# rate = []
# print(len(data))
# for i in range(len(data)-1):
#     j = (data[i+1]-data[i])/data[i]
#     #rate.append(j)
#     print(j)

# coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.api import tsa
# data2 = [6.46,6.00,6.29,6.25,8.43,8.81,9.42,10.01,10.23,10.80]
# data2 = [18.926724,18.713092,18.499461,18.28583,18.072198,17.858563,17.644917,17.431223,17.217328,17.00258,16.784222,16.550581,16.252239]
#data2 = [37.1,38.2,5.16,27.54,29.31,51.33,41.91,-3.63,70.6,-20.29,10.17,-4.03,-4.43,-11.91,-37.9,-45.08,-64.31,-51.78,-28.65,-15.04,-1.53,14.1,23.56,20.57,26.95,45.21,47.98,50.37,13.43,10.43,10.15,-2.97,-5.04]
data2 = [302.30,354.94,415.68,517.45 ,634.89 ,743.05 ,897.72 ,1298.77 ,1533.60 ,1960.30 ,2258.60 ,2493.40 ,2665.10 ,2834.06 ]
#data2 = [283.9,290.2,317.3,344.8,406.1,492.8,584.4,647.6,716.9,773.1,825.5,849.3,952.2,989.2]
def generate_data(start_date, end_date):
    df = pd.DataFrame(data2, columns=['i'],
                      index=pd.date_range(start_date, end_date, freq='D'))

    return df

# data = pd.DataFrame(data2,columns=['i'],index=list("abcdefghijklmnopqrstuvwxyz0123456"))
data = generate_data('20170601', '20170614')
data = data.astype('float64')
print(data)

data.plot()
plt.show()
#绘制自相关图
plot_acf(data).show()
plt.show()

# 差分运算
# 默认1阶差分
data_diff = data.diff()
# 差分后需要排空，
data_diff = data_diff.dropna()

data_diff.plot()
plt.show()


plot_acf(data_diff).show()
plot_pacf(data_diff).show()
plt.show()
print(data_diff)

# model = ARIMA(data, (1,1,1)).fit()
# #model.summary2()        #生成一份模型报告
# model.forecast(12)

arima = ARIMA(data, order=(1,1,0))
result = arima.fit()
# print(result.aic, result.bic, result.hqic)
# plt.plot(data_diff)
# plt.plot(result.fittedvalues, color='red')
# # #plt.title('ARIMA RSS: %.4f' % sum(result.fittedvalues - data_diff['i']) ** 2)
# plt.show()

# # ARIMA   Ljung-Box检验 -----模型显著性检验，Prod> 0.05，说明该模型适合样本
# resid = result.resid
# r, q, p = tsa.acf(resid.values.squeeze(), qstat=True)
# print(len(r), len(q), len(p))
# test_data = np.c_[range(1, 31), r[1:], q, p]
# table = pd.DataFrame(test_data, columns=['lag', 'AC', 'Q', 'Prob(>Q)'])
# print(table.set_index('lag'))
# 模型预测
result.summary2()
pred = result.predict('20170614','20170618',dynamic=True,typ='levels')
print(pred)




