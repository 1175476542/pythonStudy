# 多个条件
stu_id: int = int(input("请输入学号："))
if (stu_id >= 0) and (stu_id < 10):
    print("你是一年级学生")
elif (stu_id < 100) and (stu_id >= 10):
    print("你是二年级学生")
else:
    print("输入有误")