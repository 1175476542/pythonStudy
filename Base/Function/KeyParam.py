# 关键字参数
def user_info(name,age,gender):
    print(f'你的名字是{name},你{age}岁了,你是{gender}')
user_info('cxy',age=18,gender='male')
user_info('cxy',gender='male',age=18)