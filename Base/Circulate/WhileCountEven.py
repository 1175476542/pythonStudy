# 用while实现1-100的偶数累加
i = 0
total = 0
while i<=100:
    if i% 2 == 0:
        total += i
    i += 1
print(total)