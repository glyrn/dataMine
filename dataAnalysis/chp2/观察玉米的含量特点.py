import matplotlib
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

# [观察玉米含量特点]

dataY1=sio.loadmat("./NIRcorn.mat")

# 玉米的含量特点保存在cornprop表中

prop = dataY1['cornprop']

# 设置横坐标 （自变量)
X = np.arange(0, 80)

# 设置纵坐标 （因变量）

water = prop[:,0] # 第一列 水分
oil = prop[:,1] # 第二列 油脂
protein = prop[:,2] # 第三列 蛋白质
starch = prop[:,3] # 第四列 淀粉

# 绘制

matplotlib.rc("font", family="DengXian")

plt.grid(which='major', axis='both', color='black', linewidth=0.5)


plt.plot(X, water, color='blue', label='水分')

plt.plot(X, oil, color='red', label='油脂')

plt.plot(X, protein, color='green', label='蛋白质')

plt.plot(X, starch, color='black',label='淀粉')

plt.xlabel('玉米样本')
plt.ylabel('物质含量')

plt.legend(loc='upper right')
plt.show()