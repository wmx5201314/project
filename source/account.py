#{'username': 'admin','passwd':'admin','cartnumber':123,'quota':10000,'used':0,'repay_lixi': 0,'withdraw_quota': 0.5,'withdraw_lixi':0.05,'level':1}

import  sys
import os
import file_methed

path=os.path.dirname(os.getcwd())
print(path)
template={'username': None,'passwd':None,'cartnumber':None,'quota':10000,'used':0,'repay_lixi': 0,'withdraw_quota': 0.5,'withdraw_lixi':0.05,'level':1}

def login(username,password):
    #登录功能
    account_txt="{}\\db\\{}.txt".format(path,username)
    if os.path.exists(account_txt):
        data=file_methed.file_load(account_txt)
        if password==data['passwd']:
            print("登录成功")
            return data
    else:
        print("用户不存在")

def registry(username,password,cartnumber):
    #注册功能
            data=template
            data['username']=username
            data['passwd']=password
            data['cartnumber']=cartnumber
            account_txt="{}\\db\\{}.txt".format(path,username)  #用户信息存储地址
            file_methed.file_write(account_txt,data,'w')  #写入到用户文件
            print("注册成功")

