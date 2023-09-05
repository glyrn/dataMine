import numpy as np

# 创建数组的不同方式

# 创建一维数组
array = np.arange(20)
print(array)

# 输出结果：

# array([0,  1,  2,  3,  4,
#        5,  6,  7,  8,  9,
#        10, 11, 12, 13, 14,
#        15, 16, 17, 18, 19])


# 创建二维数组


array = np.arange(20).reshape(4,5)

# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14],
#        [15, 16, 17, 18, 19]])


# 创建多维数组 同理

array = np.arange(27).reshape(3,3,3)

# array([[[ 0,  1,  2],
#         [ 3,  4,  5],
#         [ 6,  7,  8]],

#        [[ 9, 10, 11],
#         [12, 13, 14],
#         [15, 16, 17]],

#        [[18, 19, 20],
#         [21, 22, 23],
#         [24, 25, 26]]])


# 全0 数组
np.zeros((2,4))

# 全1 数组
np.ones((3,4))

# 随机数组
np.empty((2,3))
# 这个数组的取值取决于内存的状态














