import json

from src.db.constants import FILE_DIR


def connect_r(data_name):
    print("数据库获取信息中。。。")
    with open(FILE_DIR + "/" + data_name, 'r') as amt_o:
        amt = json.load(amt_o)
        return amt


