import numpy as np
import matplotlib.pyplot as plt
print("hello world !!!")

a = np.zeros(1)

print(a)



# 使用列表或者是元组创建矩阵
my_array = np.array([1, 2, 3, 4, 5])
print(my_array.shape)
print(my_array.dtype)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

result = array1 + array2
print(result)  # 输出：[5 7 9]


matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.dot(matrix1, matrix2)
print(result)
print(matrix1 @ matrix2)



class stu:
  def __init__(self, name):
    self.name = name
  def say(self):
    self.apple = 1  # 隐式声明成员变量
    print(self.apple)




o = stu("a")

o.say()

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()








