import sys
import os
import account
import file_methed
from credit_cart_manage import cart_manage
path=os.path.dirname(os.getcwd())
config_path="{}\\config".format(path)
sys.path.append(config_path)
from setting import account_info

def main():
    print("\t\t\t\t\t--------ATM--------")
    global account_info
    if account_info['username']==None:
        print("请先登录（1.登录，2.注册）")
        op=input(">>:")
        if op.isdigit():
            op=int(op)
            if op==1:
                username=input("username:")
                password=input("password:")
                account_info=account.login(username,password)
                if account_info is None:
                    exit()
                else:
                    cart_manage(username)
            elif op==2:
                username = input("username:")
                password = input("password:")
                cart=input("cartnumber:")
                account.registry(username,password,cart)
                account_txt = "{}\\db\\{}.txt".format(path, username)
                account_info=file_methed.file_load(account_txt)
                cart_manage(username)
        else:
            print("输入错误")
    else:
        cart_manage(account_info['username'])
main()