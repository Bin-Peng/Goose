import json

#from db.constants import FILE_DIR
from src.db.constants import FILE_DIR


def connect_r(data_name):
    print("连接数据库。。。")
    with open(FILE_DIR + "/" + data_name, 'r') as amt_o:
        amt = json.load(amt_o)
        return amt


