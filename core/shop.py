import os
import datetime
import login,xinyongka
from login import login_user
path=os.getcwd()
s_path=os.path.dirname(path)
db_path="{}\\db".format(s_path)
usertxt="{}\\user.txt".format(db_path)
credit_card_txt="{}\\credit_card.txt".format(db_path)
op_log_txt="{}\\op_log.txt".format(db_path)
shopping_car="{}\\shopping_car".format(db_path)
shangping_list = [
    ["苹果手机",5000],
    ["智能手表",500],
    ["ipad",3000],
    ["烧饼",5],
    ["啤酒",6]
]


user=login_user

def get_balance(user):
    kahao=xinyongka.kahao(user)
    with open(credit_card_txt,'r',encoding='utf-8')as f:
        f=f.read()
        f_dict=eval(f)
        balance=f_dict[kahao]['shengyu']
        return balance
def new_balance(kahao,balance):
    with open(credit_card_txt, 'r', encoding='utf-8') as f:
        f=f.read()
        f_dict=eval(f)
    f_dict[kahao]['shengyu']=balance
    f_dict[kahao]['used']=f_dict[kahao]['quota']-f_dict[kahao]['shengyu']
    with open(credit_card_txt,'w',encoding='utf-8') as f:
        f.write(str(f_dict))
def shop_op(user):
    sp_op = input("1.继续购买，2.返回首页，3.查询余额，4.购物车")
    if sp_op.isdigit():
        sp_op = int(sp_op)
        if sp_op == 1:
            sp_list()
        elif sp_op == 2:
            from main import start
            start()
        elif sp_op == 3:
            print("余额：{}".format(get_balance(user)))
            shop_op(user)
        elif sp_op == 4:
            sp_car = "{}\\{}".format(shopping_car, user)
            with open(sp_car, 'r', encoding='utf-8') as f:
                f = f.read()
                print(f)
            shop_op(user)
    else:
        print("请输入数字")
    shop(user)

def shop(user):
    balance=get_balance(user)
    shop_num=input("请输入购买商品编号:")
    if shop_num.isdigit():
        shop_num=int(shop_num)
        if balance>=shangping_list[shop_num][1] and shop_num<len(shangping_list):
            balance-=shangping_list[shop_num][1]
            kahao = xinyongka.kahao(user)
            new_balance(kahao,balance)
            print("购买成功")
            shopping_cart(user,shangping_list[shop_num][0],shangping_list[shop_num][1])
            now=xinyongka.now_time()
            op_log="{} user:{} 购买操作 商品：{} 价格：{} shengyu:{}\n".format(now,user,shangping_list[shop_num][0],shangping_list[shop_num][1],get_balance(user))
            xinyongka.wirte_log(op_log)
            shop_op(user)
        else:
            print("你的余额不足以购买此商品")
            now = xinyongka.now_time()
            op_log = "{} user:{} 购买失败 商品：{} 价格：{} shengyu:{}\n".format(now, user, shangping_list[shop_num][0],shangping_list[shop_num][1], get_balance(user))
            xinyongka.wirte_log(op_log)
            shop(user)
    else:
        print("输入错误")
        now = xinyongka.now_time()
        op_log="{} user:{} 输入错误  输入：{}".format(now,user,shop_num)
        xinyongka.wirte_log(op_log)
        shop(user)

def shopping_cart(user,sp_name,sp_price):
    shopping_car_txt="{}\\{}".format(shopping_car,user)
    if os.path.exists(shopping_car_txt):
        with open(shopping_car_txt,'a',encoding='utf-8')as f:
            now=xinyongka.now_time()
            record="{} 商品：{}，价格：{}".format(now,sp_name,sp_price)
            f.write(record+"\n")
    else:
        with open(shopping_car_txt,'w',encoding='utf-8')as f:
            now=xinyongka.now_time()
            record="{} 商品：{}，价格：{}".format(now,sp_name,sp_price)
            f.write(record+"\n")


def sp_list():
    for index, i in enumerate(shangping_list):
        print(index, i)

def main():
    global user
    from login import  login_user
    user=login_user
    if user!=0:
        sp_list()
        shop(user)
    else:
        if os.path.exists(usertxt):
            print("请先登录")
            user=login.login()
            sp_list()
            shop(user)
        else:
            print("请先注册")
            login.reg()

