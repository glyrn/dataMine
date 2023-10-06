from 导入数据 import iris
# 数据集最大值最小值,以及分位点统计量
print(iris.describe())
# 转置
print(iris.describe().T)