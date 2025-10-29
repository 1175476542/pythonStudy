# 三目运算符
import random

num = int(input("请输入数字："))
value = random.randint(1, 100)
print(f"你的值为：{num},大于等于{value}")if(num >= value) else print(f"你的值为：{num},小于{value}")