# 不定长参数
# args是元组类型
# 位置参数
def user_info(*args):
    print(args)
    # print(args[0])
user_info('cxy',18)
user_info('cxy')

# 关键字参数
def user_info2(**kwargs):
    print(kwargs)
    print(type(kwargs)) # 字典
user_info2(name = 'cxy',age = 18,gender = 'male')
user_info2(name = 'cxy',age = 18)

