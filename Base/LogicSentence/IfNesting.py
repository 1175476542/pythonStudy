# if嵌套
isBroke = int(input("您的手机屏幕碎了吗？1.碎了 2.没碎"))
if isBroke == 1:
    isMoney = int(input("您有钱吗？1.有 2.没有"))
    if isMoney == 1:
        print("修好了")
    elif isMoney == 2:
        print("没钱修个几把")
    else:
        print("输入出错")
elif isBroke == 2:
    print("没碎修个几把")
else:
    print("输入出错")