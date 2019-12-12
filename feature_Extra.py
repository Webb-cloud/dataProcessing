"""特征工程，对数据进行处理使其符合算法需要"""
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
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import jieba
import xlrd


def dictvec():
    # 字典抽取API,对字典进行特征抽取
    dict = DictVectorizer()
    data = dict.fit_transform([{'city':'beijing','tem':'100'},
                               {'city':'xiamen','tem':'80'},
                               {'city':'nanjing','tem':'20'}])
    print(dict.get_feature_names())
    print(data.toarray())
    return  None

def cutword():
    #对文本进行特征抽取，先进行分词
    data1 = ["life is short,i use python","life is long,i do not use python"]
    data2 = jieba.cut(data1)
    data = list(data2)
    return data

def countvec():
    #对文本进行特征抽取，即特征值化
    cv = CountVectorizer()
    data = cv.fit_transform(["life is short,i learn python","life is long,i learn python"])
    data1 = cv.get_feature_names()
    print(data1)
    print(data.toarray())
    return None

def tfidfvec():
    #用tf-idf的方法进行文本特征值抽取
    dict = TfidfVectorizer()
    data = dict.fit_transform(["life is long,i learn python","life is short,i learn python"])
    data1 = dict.get_feature_names()
    print(data)
    print(data1)
    return None

#数据归一化
def minmaxvec():
    minmax = MinMaxScaler()
    data = minmax.fit_transform([[12,3,4],
                                [1,3,4],
                                [2,4,6]])
    print(data)
    return None

def pca(f):
    #对特征进行主成分分析
    pca1 = PCA(n_components=0.9)
    #fit_transform里面是二维数组
    data = pca1.fit_transform(f)
    print(data)

    #pd的dataframe转换为数组？
    return None

def read_data():
    #进行主成分分析之前读取数据
    data = pd.read_excel("fsi-2006.xlsx")
    data = data.to_dict(orient='records')
    print(data)
    return data

def knncls():
    #读取数据
    data = pd.read_csv("")
    print(data.head(10))
    #处理数据，缩小数据
    data = data.query("x > 1.0 & x < 1.25 & y >1.5 & y < 1.75")
    # #处理时间戳
    time_value = pd.to_datetime(data['time'],unit = 's')
    print(time_value)
    #转换字典
    time_value = pd.DatetimeIndex(time_value)
    data['day'] = time_value.day

    #删除特征
    data.drop(['time'],axis=1)
    #把数量小于n个的删除
    place_count = data.groupby('place_id')
    tf = place_count[place_count.row_id >3].reset_index()
    # 取出在tf中的并且在data中的数据
    data = data[data['place_id']].isin(tf.place_id)

    y = data['place_id']
    x = data.drop(['palce_id'],axis= 1 )
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


def naviebayes():
    news = fetch_20newsgroups(subset='all')
    x_train,x_test,y_train,y_test = train_test_split(news.data,news.target,test_size= 0.25 )
    #tf-idf对数据集进行特征抽取
    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)
    x_test = tf.transform(x_test)
    print(tf.get_feature_names())

    mlt = MultinomialNB(alpha= 1.0)
    mlt.fit(x_train,y_train)
    y_predict = mlt.predict(x_test)
    print(y_predict)
    print(mlt.score())


if __name__ == "__main__":
     read_data()
