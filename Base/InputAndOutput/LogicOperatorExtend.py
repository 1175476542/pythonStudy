# 拓展
a = 0
b = 1
c = 2
# and运算符时，只要有一个数值为0，那么表达式就为0,否则为最后一个非0数字
print(a and b)
print(b and a)
print(a and c)
print(c and a)
print(b and c)
print(c and b)
# or运算符中只有所有值为0才为0，否则结果为第一个非0数字
print(a or b)
print(b or c)
print(a or c)