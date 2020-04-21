import json,os
import xinyongka
path=os.getcwd()
s_path=os.path.dirname(path)
db_path="{}\\db".format(s_path)
usertxt="{}\\user.txt".format(db_path)
login_user=0
def login():
    username = input("账号:").strip()
    password = input("密码:").strip()
    f=open(usertxt,"r",encoding="utf-8")
    f=f.read()
    f_dict=eval(f)
    if username in f_dict:
        if password==f_dict[username]['password']:
            global login_user
            login_user=username
            print("已登录")
            now = xinyongka.now_time()
            op_log = "{} 登录成功 username:{} password:{} \n".format(now, username, password)
            xinyongka.wirte_log(op_log)
            return username
        else:
            print("密码错误")
            now = xinyongka.now_time()
            op_log = "{} 登录失败，密码错误 username:{} password:{} \n".format(now, username, password)
            xinyongka.wirte_log(op_log)
            login()
            return 0
    else:
        print("用户不存在")
        now = xinyongka.now_time()
        op_log = "{} 登录失败，用户名不存在 username:{}\n".format(now, username)
        xinyongka.wirte_log(op_log)
        login()
        return 0
def reg():
    username = input("新账号:").strip()
    password = input("密码:").strip()
    kahao = input("信用卡号：").strip()
    info = "{0}'{1}':{0}'password':'{2}','kh':'{3}'{4}{4}".format('{', username, password, kahao, '}')
    if os.path.exists(usertxt):
        with open(usertxt, 'r', encoding="utf-8") as f:
            f = f.read()
        f_dict = eval(f)
        info = eval(info)
        if username not in f_dict:
            for i in info:
                f_dict[i] = info[i]
            with open(usertxt, 'w', encoding="utf-8") as f1:
                f1.write(str(f_dict))
                xinyongka.credit_card_init(kahao)
                print("注册成功，赶紧登录吧")
                now = xinyongka.now_time()
                op_log="{} 注册成功 username:{} password:{} kahao:{}\n".format(now,username,password,kahao)
                xinyongka.wirte_log(op_log)
        else:
            print("用户名已存在，请重新注册")
            now = xinyongka.now_time()
            op_log = "{} 注册时用户名重复 username:{} \n".format(now, username)
            xinyongka.wirte_log(op_log)
            reg()
        login()
    else:
        with open(usertxt, 'w', encoding="utf-8") as f:
            f.write(info)
            xinyongka.credit_card_init(kahao)
            print("注册成功,赶紧登录吧")
            now = xinyongka.now_time()
            op_log = "{} 注册成功 username:{} password:{} kahao:{}\n".format(now, username, password, kahao)
            xinyongka.wirte_log(op_log)
        login()
