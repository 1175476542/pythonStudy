# 集合删除数据
s1 = {1,2,3,4,5,6}

# 1.remove()
# s1.remove(1)# {2, 3, 4, 5, 6}
# print(s1)
# s1.remove(1)# 报错
# print(s1)
# 2.discard()
# s1.discard(1)# {2, 3, 4, 5, 6}
# print(s1)
# s1.discard(1)# {2, 3, 4, 5, 6}
# print(s1)
# 3.pop()
del_num = s1.pop()
print(del_num)
print(s1)