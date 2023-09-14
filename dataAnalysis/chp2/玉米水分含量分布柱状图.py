import matplotlib
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

# 导入数据
dataY1=sio.loadmat("./NIRcorn.mat")

# [玉米水分 分布柱状图 -> 采用分区 然后统计范围中的数量]

# 玉米水分
water = dataY1['cornprop'][:,0]

plt.hist(water, bins=[9, 9.5, 10, 10.5, 11], color="r", rwidth=0.8)

plt.title("Corn water content distribution")

plt.show()