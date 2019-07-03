#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-01 00:04
# @Author  : pengb
# @File    : db.py
# @Software: PyCharm
import json

# 读取数据库数据
from src.account.account import Account
from src.db import connect_r
from src.db.constants import FILE_DIR


class ActTable(object):
    def __init__(self):
        self.acts: dict = connect_r("Amt.json")
        self.act_names: dict = connect_r("AmtName.json")

    def add_act_name(self, name):
        if name not in self.act_names.values():
            self.act_names.setdefault("root", name)
            with open(FILE_DIR + "/" + "AmtName.json", "w") as amt_r:
                json.dump(self.act_names, amt_r)
                return True
        return False

    # 写入数据
    def add_act(self, account: Account()):
        result = self.add_act_name(account.actName)

        if not result:
            print("账户已存在，账户添加失败，account: ", self.acts.get(account.actName))
            return False
        self.acts.setdefault(account.actName, account.money)
        with open(FILE_DIR + "/Amt.json", "w") as amt_n:
            json.dump(self.acts, amt_n)
            print("账户添加成功,account: ", self.acts.get(account.actName))
        return True

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
