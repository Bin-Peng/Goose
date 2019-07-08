#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-01 00:04
# @Author  : pengb
# @File    : db.py
# @Software: PyCharm
import json

from src.account.account import Account
from src.db import connect_r, R
from src.db.constants import FILE_DIR


# 读取数据库数据


class ActTable(object):
    def __init__(self):
        self.acts: dict = connect_r("Amt.json")

    # 写入数据
    def add_act(self, account: Account()):
        R.acquire()
        if account.actName in self.acts.keys():
            print("账户已存在，账户添加失败，account: ", self.acts.get(account.actName))
            return False
        self.acts.setdefault(account.actName, account.__dict__)
        R.release()
        return True

    def set_act_all(self, act_all):
        with open(FILE_DIR + "/Amt.json", "w") as amt_n:
            json.dump(act_all, amt_n)
            print("全账户更新成功")

    def dele_act(self, act_name):
        self.acts.pop(act_name)
        with open(FILE_DIR + "/Amt.json", "w") as amt_n:
            json.dump(self.acts, amt_n)
            return self.acts

    # 获取单账户数据
    def get_act(self, name):
        pass

    # 获取所有账户数据
    def get_act_all(self):
        return self.acts

    def get_lock(self):
        return R
