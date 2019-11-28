from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier as knn
import pandas as pd
import jieba
import xlrd

def knncls():
    #读取数据
    data = load_iris()
    #print(data)
    x = data['data']
    y = data['target']
    print(x)
    print(y)
    #处理数据，缩小数据
    # data = data.query("x > 1.0 & x < 1.25 & y >1.5 & y < 1.75")
    # #处理时间数据
    # time_value = pd.datetime(data['time'],unit = 's')
    # print(time_value)
    # #转换字典
    # time_value = pd.DatetimeIndex(time_value)
    # data['day'] = time_value.day
    # #删除特征
    # data.drop(['time'],axis=1)
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)
    #标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    knn.fit(x_train,y_train)

    y_predict = knn.predict(x_test)
    print(y_predict)
    #打印准确率
    print(knn.score(x_test,y_test))



if __name__ == "__main__":
    knncls()
