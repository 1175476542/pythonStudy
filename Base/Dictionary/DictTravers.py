# 字典遍历
dict1 = {"name":"cxy","age":26,"description":"dreams come true"}
# 遍历字典的key
for key in dict1.keys():
    print(key)
# 遍历字典的value
for value in dict1.values():
    print(value)
# 遍历字典键值对
for item in dict1.items():
    print(item)
    print(item[0],end="\t")
    print(item[1],end="\n")
# 遍历字典键值对(拆包)
print("---------------")
for items in dict1.items():
    for item in items:
        print(item)
# 遍历字典键值对(拆包)
print("==================")
for key,item in dict1.items():
    print(f'{key}=>{item}')