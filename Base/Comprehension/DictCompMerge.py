# 合并列表为字典

l1 = ['name','age','gender','id']
l2 = ['cxy','26','男']

dict1 = {l1[i]:l2[i] for i in range(len(l2))}
print(dict1)