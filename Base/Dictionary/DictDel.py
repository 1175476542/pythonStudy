# 删除字典或键值对
dict1 = {"name":"cxy","age":26,"description":"dreams come true"}

del dict1["name"]
print(dict1)# {'age': 26, 'description': 'dreams come true'}

dict1.clear()
print(dict1)# {}

del dict1
print(dict1)# 报错