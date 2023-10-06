from sklearn import datasets
import pandas as pd
iris_datas=datasets.load_iris()

#获取鸢尾花数据集
print(pd.concat([pd.DataFrame(iris_datas.data),pd.DataFrame(iris_datas.target)],axis=1))

iris = pd.DataFrame(iris_datas.data, columns=['SpealLength', 'Spealwidth', 'PetalLength', 'PetalLength'])

iris.shape
print(iris.head()) #读取数据的头5个数值
print(iris.tail()) #读取数据的后5个数值

print(iris.info()) #读取完整数据数值

print(iris.describe())

print(iris.describe().T) #转置了

from collections import Counter, defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

style_list = ['o', '^', 's']  # 设置点的不同形状，不同形状默认颜色不同，也可自定义
data = iris_datas.data
labels = iris_datas.target_names
cc = defaultdict(list)
for i, d in enumerate(data):
    cc[labels[int(i / 50)]].append(d)
p_list = []
c_list = []
for each in [0, 2]:
    for i, (c, ds) in enumerate(cc.items()):
        draw_data = np.array(ds)
        p = plt.plot(draw_data[:, each], draw_data[:, each + 1], style_list[i])
        p_list.append(p)
        c_list.append(c)
    plt.legend(map(lambda x: x[0], p_list), c_list)
    plt.title('鸢尾花花瓣的长度和宽度') if each else plt.title('鸢尾花花萼的长度和宽度')
    plt.xlabel('花瓣的长度(cm)') if each else plt.xlabel('花萼的长度(cm)')
    plt.ylabel('花瓣的宽度(cm)') if each else plt.ylabel('花萼的宽度(cm)')
    plt.show()

#构建直方图
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
dataset.hist() #数据直方图histograms

#构建散点图
dataset.plot(x='sepal-length', y='sepal-width', kind='scatter')  #width深度，length长度

#构建KDE图
dataset.plot(kind='kde')
plt.show()