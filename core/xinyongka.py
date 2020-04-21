import os

import datetime
import login
from login import login_user
path=os.getcwd()
s_path=os.path.dirname(path)
db_path="{}\\db".format(s_path)
usertxt="{}\\user.txt".format(db_path)
credit_card_txt="{}\\credit_card.txt".format(db_path)
op_log_txt="{}\\op_log.txt".format(db_path)
user=login_user
def kahao(user):
    with open(usertxt,'r',encoding='utf-8') as f:
        f=f.read()
        f_dict=eval(f)
        khao=f_dict[user]['kh']
        return khao

def now_time():
    now_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now_time

def info(username):
    print("------用户：{}-------".format(username))
    kh=kahao(username)
    with open(credit_card_txt,'r',encoding='utf-8') as f:
        f=f.read()
    credit_card_dict=eval(f)
    quota=credit_card_dict[kh]['quota']
    used=credit_card_dict[kh]['used']
    shengyu=credit_card_dict[kh]['shengyu']
    print('''信用卡卡号：{}
总额度:{}
已使用:{}
可用额度：{}
    '''.format(kh,quota,used,shengyu))
    now=now_time()
    op_log="{0} user:{1} 查询操作 kahao:{2} quota：{3} used：{4} shengyu：{5}\n".format(now,username,kh,quota,username,shengyu)
    wirte_log(op_log)
def credit_card_init(kh):
    kh_dict={kh:{'quota':10000,'used':0,'shengyu':10000}}
    if os.path.exists(credit_card_txt):
        with open(credit_card_txt,'r',encoding='utf-8') as f:
            f=f.read()
            f_dict=eval(f)
        with open(credit_card_txt,'w',encoding='utf-8') as f1:
            f_dict[kh]=kh_dict[kh]
            f1.write(str(f_dict))
            print("初始化成功！额度：{}".format(kh_dict[kh]['quota']))
            now=now_time()
            op_log="{} kahao:{} 初始化操作 quota:{} used:{} shengyu:{}\n".format(now,kh,kh_dict[kh]['quota'],kh_dict[kh]['used'],kh_dict[kh]['shengyu'])
            wirte_log(op_log)
    else:
        with open(credit_card_txt,'w',encoding='utf-8') as f:
            f.write(str(kh_dict))
            print("初始化成功！额度：{}".format(kh_dict[kh]['quota']))
            now = now_time()
            op_log = "{} kahao:{} 初始化操作 quota:{} used:{} shengyu:{}\n".format(now, kh, kh_dict[kh]['quota'],kh_dict[kh]['used'], kh_dict[kh]['shengyu'])
            wirte_log(op_log)
#{'123':{'quota': 10000,'used': 0,'shengyu': 10000}}
def wirte_log(log):
    if os.path.exists(op_log_txt):
        with open(op_log_txt,'a',encoding='utf-8') as f:
            f.write(log)
    else:
        with open(op_log_txt,'w',encoding='utf-8') as f:
            f.write(log)
def Repayment(user):
    with open(credit_card_txt,'r',encoding='utf-8')as f:
        f=f.read()
        f_dict=eval(f)
        kh=kahao(user)
        used=f_dict[kh]['used']
        used=int(used)
        if used!=0:
            print("你已使用{}元额度".format(used))
            rp=input("请输入还款金额:")
            if rp.isdigit():
                rp=int(rp)
                if rp<=used:
                    used=used-rp
                    shengyu=f_dict[kh]['shengyu']+rp
                    f_dict[kh]['used']=used
                    f_dict[kh]['shengyu']=shengyu
                    with open(credit_card_txt,'w',encoding='utf-8')as f1:
                        f1.write(str(f_dict))
                        print("还款成功！")
                        now=now_time()
                        op_log="{} 还款成功 user:{} 还款金额：{} 剩余额度：{}\n".format(now,user,rp,shengyu)
                        wirte_log(op_log)
                else:
                    print("土豪，你还多了！")
            else:
                print("请输入正确金额")
        else:
            print("账单已还清")

def qukuan(user):
    with open(credit_card_txt, 'r', encoding='utf-8')as f:
        f = f.read()
        f_dict = eval(f)
        kh = kahao(user)
        shengyu=f_dict[kh]['shengyu']
        print("你的剩余额度为{}".format(shengyu))
        qk=input("请输入取款金额:")
        if qk.isdigit():
            qk=int(qk)
            shengyu=f_dict[kh]['shengyu']-qk
            used=f_dict[kh]['used']+qk
            f_dict[kh]['shengyu']=shengyu
            f_dict[kh]['used']=used
            with open(credit_card_txt, 'w', encoding='utf-8')as f:
                f.write(str(f_dict))
                print("取款成功")
                now = now_time()
                op_log = "{} 取款成功 user:{} 取款金额：{} 剩余额度：{}\n".format(now, user, qk, shengyu)
                wirte_log(op_log)
        else:
            print("金额不正确，请输入整数")

def main():
    global user
    while True:
        from login import login_user
        user=login_user
        if user!=0:
            print("1.查询信息,2.还款，3.取款,4.返回首页,5.退出")
            op=input("请选择你的操作")
            if op.isdigit():
                op=int(op)
                if op==1:
                    info(user)
                elif op==2:
                    Repayment(user)
                elif op==3:
                    qukuan(user)
                elif op==4:
                    from main import start
                    start()
                elif op==5:
                    exit()
                else:
                    print("请输入正确数字")
        else:
            if os.path.exists(usertxt):
                print("请先登录")
                user = login.login()
            else:
                print("请先注册")
                login.reg()
