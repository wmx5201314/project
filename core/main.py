import xinyongka,shop,login
from xinyongka import main

def start():
    print("---------欢迎来到我的程序！---------")

    while True:
        print("1.商店\n2.信用卡管理\n3.注册")
        op=input("请输入编号：")
        if op.isdigit():
            op=int(op)
            if op==1:
                shop.main()
            elif op==2:
                xinyongka.main()
            elif op==3:
                login.reg()
            else:
                print("输入错误")
        else:
            print("输入错误")
start()