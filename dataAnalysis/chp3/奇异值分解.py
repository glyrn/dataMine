import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 导入数据集
data=sio.loadmat("../chp2/NIRcorn.mat")
# 先取得前四个样本的属性  水分 油 蛋白质 淀粉值
sample_4 = data['cornprop'][0:4,:]
print(sample_4)

# SVD 分解
U, sigma, VT = np.linalg.svd(sample_4)

print("U矩阵")
print(U)
print("sigma矩阵")
print(sigma)
print("VT矩阵")
print(VT)

# 验证U矩阵是 A*A.T特征向量形成的矩阵，sigma对角阵是A*A.T特征值开根号
eigenvalue, feature_vector = np.linalg.eig(np.dot(sample_4, sample_4.T))
print("A*AT特征值")
sorted_eigenvalue = np.argsort(-eigenvalue)
print(sorted_eigenvalue[sorted_eigenvalue])
print("A*AT特征向量")
# 按照特征排序的下标号对应排序特征向量
f = feature_vector[:, sorted_eigenvalue]
print(f)
# 验证V矩阵是(A.T*A)特征向量组成的矩阵
eigenvalue, feature_vector = np.linalg.eig(np.dot(sample_4.T, sample_4))
print("A.T*A特征值")
sorted_eigenvalue = np.argsort(-eigenvalue)
print(eigenvalue[sorted_eigenvalue])
print("A.T*A特征向量")
f = feature_vector[:, sorted_eigenvalue]
print(f)

