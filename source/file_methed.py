import os
import sys
import json

def file_write(file_name,data,methed,**other):
    #文件写入
    with open(file_name,methed,encoding='utf-8') as f:
        f.write(json.dumps(data))



def file_load(file_name,**other):
    #文件读取
    with open(file_name,'r',encoding='utf-8')as f:
        f=json.loads(f.read())
        return f