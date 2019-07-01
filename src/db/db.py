#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-01 00:04
# @Author  : pengb
# @File    : db.py
# @Software: PyCharm
import json

from Goose.src.account.account import Account
from Goose.src.db.constants import FILE_DIR


def connect_r(data_name):
    with open(FILE_DIR + "/"+ data_name, 'r') as amt_o:
        amt = json.load(amt_o)
        return amt

class ActTable(object):
    def __int__(self):
        # 与数据库或者说
            self.acts: dict = connect_r("Amt.json")
            self.act_names: list = connect_r("AmtName.json")
    def add_act_name(self, name):
        if name not in self.act_names:
            self.act_names.pop(name)
            return true
        self

#写入数据
    def add_act(self, account: Account):

        self.acts.pop(account)
        with open(FILE_DIR + "/Amt.json", "w") as amt_n:
            json.dump(self.acts, amt_n)


