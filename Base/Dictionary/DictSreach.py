# 字典查找
dict1 = {"name":"cxy","age":26,"description":"dreams come true"}
# 通过key查找
print(dict1['name'])

# get()
print(dict1.get("name"))
print(dict1.get("names"))
print(dict1.get("names","查找出错"))# 查找出错
# keys
print(dict1.keys())# dict_keys(['name', 'age', 'description'])
# values()
print(dict1.values())# dict_values(['cxy', 26, 'dreams come true'])
# items()
print(dict1.items())# dict_items([('name', 'cxy'), ('age', 26), ('description', 'dreams come true')])