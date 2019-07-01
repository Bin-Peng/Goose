#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-01 00:04
# @Author  : pengb
# @File    : db.py
# @Software: PyCharm
import json



# 读取数据库数据
import Goose.src.account.account
from Goose.src.db.constants import FILE_DIR


def connect_r(data_name):
    with open(FILE_DIR + "/" + data_name, 'r') as amt_o:
        amt = json.load(amt_o)
        return amt


class ActTable(object):
    def __int__(self):
        self.acts: dict = connect_r("Amt.json")
        self.act_names: list = connect_r("AmtName.json")

    def add_act_name(self, name):
        if name not in self.act_names:
            self.act_names.pop(name)
            return True
        else:
            return False

    # 写入数据
    def add_act(self, account: Goose.src.account.account.Account):
        result = self.add_act_name(account.actName)
        if result:
            print("账户已存在，账户添加失败，account: ", self.acts.get(account.actName))
            return False
        self.acts.pop(account)
        with open(FILE_DIR + "/Amt.json", "w") as amt_n:
            json.dump(self.acts, amt_n)
            print("账户添加成功,account: ", self.acts.get(account.actName))
        return True
