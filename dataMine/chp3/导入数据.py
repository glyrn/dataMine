from sklearn import  datasets
import pandas as pd

iris_datas = datasets.load_iris()

# 获取鸢尾花数据集
print(pd.concat([pd.DataFrame(iris_datas.data), pd.DataFrame(iris_datas.target)], axis = 1))

iris = pd.DataFrame(iris_datas.data, columns=['Spalen length', 'Spa len width', 'Petal length', 'Petal width'])

# 读取数据的前5行
print(iris.head())

# 读取数据的后5行
print(iris.tail())

# 读取完整数据
print(iris.info)