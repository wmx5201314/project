import os
import sys
import file_methed

path=os.path.dirname(os.getcwd())
config_path="{}\\config".format(path)
sys.path.append(config_path)
from setting import account_info
def option():
    print('''------credit cart management-------
        1.还款(已实现)
        2.取现(已实现)
        3.查询(已实现)
        4.账单
    ''')
    op=input("请输入操作：")
    return op

def cart_manage(username):
    op_meth={
        1:repay,
        2:withdraw,
        3:info,
        4:'bill'
    }  #序列号对应函数名
    op=int(option())
    op_meth[op](username)  #按照用户输入操作执行相应函数


def repay(username):
    #还款操作
    account_txt = "{}\\db\\{}.txt".format(path, username)
    data=file_methed.file_load(account_txt)
    balance=data['quota']-data['used']
    if data['used'] !=0:       #判断已用金额
        print('\t额度：{}\n\t\t已用：{}\n\t\t剩余额度：{}'.format(data['quota'],data['used'],balance))
        repay_money=input('\t\t请输入还款金额>>:')
        if repay_money.isdigit():
            repay_money=float(repay_money)
            if repay_money<=data['used'] and repay_money>0:
                repay_money=int(repay_money)
                handling_fee=repay_money*data['repay_lixi']  #手续费
                data['used']-=repay_money-handling_fee
                file_methed.file_write(account_txt,data,'w')
                print('还款成功！本次还款：{}，手续费：{}'.format(repay_money,handling_fee))
                cart_manage(username)
            else:
                print("还款金额不正确")
                cart_manage(username)
        else:
            print("请输入正确金额")
            cart_manage(username)
    else:
        print("你不需要还款")
        cart_manage(username)
def withdraw(username):
    #取现操作
    account_txt = "{}\\db\\{}.txt".format(path, username)
    data = file_methed.file_load(account_txt)
    balance = data['quota'] - data['used']
    withdraw_quota=balance*data['withdraw_quota']   #取现额度
    print("当前剩余可用额度为：{},能取现额度：{}，手续率：{}".format(balance,withdraw_quota,data["withdraw_lixi"]))
    withdram_money=input("请输入取现金额>>:")
    if withdram_money.isdigit():
        withdram_money=float(withdram_money)
        if withdram_money<=withdram_money and withdram_money>=0:
            balance-=withdram_money         #减去取现金额
            balance-=withdram_money*data["withdraw_lixi"]   #减去利息
            data['used']=data['quota']-balance
            file_methed.file_write(account_txt, data, 'w')
            print("取现成功，取现金额：{}，手续费：{}，剩余额度：{}".format(withdram_money,withdram_money*data["withdraw_lixi"],balance))
            cart_manage(username)
        else:
            print("请输入正确金额")
            cart_manage(username)
    else:
        print("输入错误")
        cart_manage(username)

def info(username):
    #个人信息
    account_txt = "{}\\db\\{}.txt".format(path, username)
    data = file_methed.file_load(account_txt)
    balance = data['quota'] - data['used']
    withdraw_quota = balance * data['withdraw_quota']  # 取现额度
    print('''-----------个人信息------------
        username:{}
        cartnumber:{}
        quota:{}
        used_quota:{}
        withdraw_quota:{}
        withdraw_interest_rate:{}
    '''.format(data['username'],data['cartnumber'],data['quota'],data['used'],withdraw_quota,data['withdraw_lixi']))
    op=input("任意键返回>>:")
    cart_manage(username)
