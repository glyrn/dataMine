# 列表，元素可变
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
 
# print ("list1[0]: ", list1[0])
# print ("list2[1:5]: ", list2[1:5])




# 元组，元素不可变
top = (1, 2, 3)
r2 = (4, 5)
# print(top)
print(top[1:2])   # 包含左边
r3 = top + r2
# 元组不可以修改但是可以拼接
print(r3)
# 删除元组
del r3
# print(r3) 这里会发生报错

# 列表可以转换成元组





# 字典结构
dict1 = {"a":1, "b":2}
a = dict1["a"]
print(a)

# 添加字典
dict1["c"] = 2
print(dict1)

# 删除字典元素
del dict1["c"]
print(dict1)
# 清空字典
dict1.clear()
print(dict1)

# 字典中的键值限制，用数字，字符串或元组充当，但是不能使用列表
# 个人认为键值的限制在于，不能使用可以修改的变量

















