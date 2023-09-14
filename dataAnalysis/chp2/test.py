import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

# 加载数据
dataY1 = sio.loadmat("./NIRcorn.mat")
cornWavelength = dataY1["cornwavelength"]
cornSpect = dataY1["cornspect"]

# 提取波长值
X = [cornWavelength[i][0] for i in range(cornWavelength.shape[0])]

# 提取80个样本的光谱数据
spectra_data = [cornSpect[i] for i in range(cornSpect.shape[0])]

# 标准化和标准化数据
normalized_data = (spectra_data - np.min(spectra_data, axis=1)[:, np.newaxis]) / (
    np.max(spectra_data, axis=1)[:, np.newaxis] - np.min(spectra_data, axis=1)[:, np.newaxis]
)

standardized_data = (normalized_data - np.mean(normalized_data, axis=1)[:, np.newaxis]) / (
    np.std(normalized_data, axis=1)[:, np.newaxis]
)

# 创建图表和坐标轴
fig, ax = plt.subplots()

# 绘制各个样本的光谱
for i in range(5):
    ax.plot(X, standardized_data[i], label=f"样本 {i + 1}")

# 绘制所有样本的平均值作为新的线
average_spectrum = np.mean(standardized_data, axis=0)
ax.plot(X, average_spectrum, label="平均标准化吸光率", linestyle='--')

# 设置标签和标题
ax.set_xlabel("波长/nm")
ax.set_ylabel("标准化吸光率")
ax.set_title("根据玉米数据集绘制的波长-标准化吸光率曲线图")

# 设置坐标轴范围和刻度
ax.set_xlim((1100, 2500))
ax.set_ylim((-0.2, 1.2))
my_x_ticks = np.arange(1100, 2500, 100)
my_y_ticks = np.arange(-0.2, 1.2, 0.2)
ax.set_xticks(my_x_ticks)
ax.set_yticks(my_y_ticks)

# 显示图例和网格
ax.legend()
ax.grid(linestyle='-.')

# 显示图表
plt.show()
