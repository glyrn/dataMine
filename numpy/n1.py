
import numpy as np

# 这个是numpy的入门

my_array = np.zero(5)

print(my_array)

# 创建数组
# 1D Array
a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2*np.pi, 5)

print(a) # >>>[0 1 2 3 4]
print(b) # >>>[0 1 2 3 4]
print(c) # >>>[0 1 2 3 4]
print(d) # >>>[ 0.          1.57079633  3.14159265  4.71238898  6.28318531]
print(a[3]) # >>>3



# 多维数组

# MD Array,
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(a[2,4]) # >>>25


# 多维数组切片

# MD slicing
print(a[0, 1:4]) # >>>[12 13 14]
print(a[1:4, 0]) # >>>[16 21 26]
print(a[::2,::2]) # >>>[[11 13 15]
                  #     [21 23 25]
                  #     [31 33 35]]
print(a[:, 1]) # >>>[12 17 22 27 32]

# 数组属性

# Array properties
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(type(a)) # >>><class 'numpy.ndarray'>
print(a.dtype) # >>>int64
print(a.size) # >>>25
print(a.shape) # >>>(5, 5)
print(a.itemsize) # >>>8
print(a.ndim) # >>>2
print(a.nbytes) # >>>200


# 关于使用数组

# 注意 矩阵中的乘法不是使用乘法运算符 而是使用dto方法

# Basic Operators
a = np.arange(25)
a = a.reshape((5, 5))

b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
b = b.reshape((5,5))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b) print(a > b)

print(a.dot(b))


# 数组的特殊运算符
# dot, sum, min, max, cumsum
a = np.arange(10)

print(a.sum()) # >>>45
print(a.min()) # >>>0
print(a.max()) # >>>9
print(a.cumsum()) # >>>[ 0  1  3  6 10 15 21 28 36 45]


# 花式索引

# Fancy indexing
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]
print(a) # >>>[ 0 10 20 30 40 50 60 70 80 90]
print(b) # >>>[10 50 90]




