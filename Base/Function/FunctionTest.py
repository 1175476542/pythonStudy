pwd = '123456'
balance = 10000
flag = True

def login(inp):
    # inp = input("请输入密码：")
    if inp == pwd:
        print("登陆成功")
        # view()
    else:
        print("用户名或密码不正确")
        view()

def view():
    print("1.登陆")
    print("2.查询")
    print("3.取款")
    print("4.存款")
    print("5.退出")

def exit():
    global flag
    flag = False
    print("你已退出程序")

def find():
    out = int(input("请输入你的取款金额："))
    global balance
    balance -= out
    query()
    return balance

def query():
    print(f"你的余额剩余:{balance}")

def deposit(depositMoney):
    global balance
    balance += depositMoney
    query()
    return balance

def main():
    view()
    inp = input("请选择服务：")
    if inp == '1':
        pwd = input("请输入你的密码：")
        login(pwd)
    if inp == '2':
        query()
    if inp == '3':
        find()
    if inp == '4':
        depositMoney = int(input("请输入你存款数："))
        deposit(depositMoney)
    if inp == '5':
        exit()

while flag:
    # view()
    main()