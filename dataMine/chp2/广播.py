import numpy as np

# 创建一个形状为(3, 3)的数组
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# 创建一个形状为(3,)的一维数组
# 这里由于形状不匹配，会隐式使用广播
arr2 = np.array([10, 20, 30])



# 对两个数组进行加法操作，广播arr2使其形状与arr1匹配
result = arr1 + arr2

print(result)
