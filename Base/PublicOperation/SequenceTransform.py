list1 = [1,2,3,4,5]
s1 = {1,2,3,4,5}
t1 = (1,2,3,4,5)

print(tuple(list1))
print(tuple(s1))
print(list(s1))
print(list(t1))
print(set(list1)) # 去重且无序
print(set(t1))