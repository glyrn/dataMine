import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# 绘制 波长-吸光率 曲线图

# step1 读取数据集
# 在pycharm中可以通过变量监视器查看变量插入与否
# 此处引入的数据是字典型数据, 需要引用其中的值
dataY1=sio.loadmat("./NIRcorn.mat")

# print(dataY1)

        # 注意这里的mat是一个树形结构，中间包含多个表
        # -- 波长


# step2 数据的选取和存储
# X用于存储自变量(波长离散值, 1100-2500, 单位是nm)
X = []
cornWavelength = dataY1["cornwavelength"] # 读取波长数据表

# 存储全部取到的波长值
for i in range(0, cornWavelength.__len__()):
    X.append(cornWavelength[i][0]) # 因为都是第一列 所以是[i][0]
# Yi(i∈{1, 2, 3, 4, 5})用于存储因变量(5个样本的不同波长吸光率数据)

# 选取第1, 17, 33, 49, 65号样本
Y1 = []
Y2 = []
Y3 = []
Y4 = []
Y5 = []
cornSpect = dataY1["cornspect"]
# 存储10个样本的对应波长值的吸光率数值  --> 注意 这个表是横向的 每一组数据都是一行 每一行都有700个数据 代表不同波长下的吸光度
for i in range(0, 700):
    Y1.append(cornSpect[0][i])
    Y2.append(cornSpect[16][i])
    Y3.append(cornSpect[32][i])
    Y4.append(cornSpect[48][i])
    Y5.append(cornSpect[64][i])

# 定义一个函数来对样本数据进行中心化，标准化和归一化
def dataProcesssing(Y: [float]) -> [float]:
    Y_mean = np.mean(Y)  # 求取均值
    Y_std = np.std(Y)  # 求取标准差
    Y_final = [(y - Y_mean) / Y_std for y in Y]  # 中心化和标准化
    Y_normalized = normalize(Y_final)  # 归一化
    return Y_normalized

# 归一化
def normalize(Y:[float]) -> [float]:
    # 将输入列表转换成numpy数组格式
    Y_arr = np.array(Y)
    # 找到最大值和最小值
    min = np.min(Y_arr)
    max = np.max(Y_arr)
    # 归一化
    normalized = (Y_arr - min) / (max - min)
    # 转换成列表形式
    Y_normalized = normalized.tolist()
    return Y_normalized

# 对样本数据分别进行中心化
Y1_final = dataProcesssing(Y1)
Y2_final = dataProcesssing(Y2)
Y3_final = dataProcesssing(Y3)
Y4_final = dataProcesssing(Y4)
Y5_final = dataProcesssing(Y5)

# step3 数据可视化
# 解决字体问题

matplotlib.rc("font",family='DengXian')

# 题图和坐标轴信息
plt.xlabel("波长/nm")
plt.ylabel("吸光率")
plt.title("根据玉米数据集绘制的波长-吸光率曲线图")

# 规定X,y上下限数值和刻度
plt.xlim((1100, 2500))
plt.ylim((0, 0.9))

# 设置坐标轴刻度
my_x_ticks = np.arange(1100, 2500, 100)
my_y_ticks = np.arange(0, 0.9, 0.05)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)

plt.plot(X, Y1, label="样本1")
plt.plot(X, Y2, label="样本17")
plt.plot(X, Y3, label="样本33")
plt.plot(X, Y4, label="样本49")
plt.plot(X, Y5, label="样本65")

plt.plot(X, Y1_final, label="样本1-预处理后")
plt.plot(X, Y2_final, label="样本17-预处理后")
plt.plot(X, Y3_final, label="样本33-预处理后")
plt.plot(X, Y4_final, label="样本49-预处理后")
plt.plot(X, Y5_final, label="样本65-预处理后")

# 显示标签
plt.legend()

# 生成网格
plt.grid(linestyle='-.')

# 绘制
plt.show()
