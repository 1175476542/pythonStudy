# 获取字典中目标数据

computers = {'DELL':199,'HUAWEI':198,'XIAOMI':200,'ACER':9999}

dict1 = {key:value for key,value in computers.items()}
print(dict1)
dict2 = {key:value for key,value in computers.items() if value >= 200}
print(dict2)