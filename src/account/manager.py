#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-02 00:49
# @Author  : Michael
# @File    : manager.py
# @Software: PyCharm
from src.db import db
from src.account.account import Account


class AccountMng:
    def __init__(self):
        self.accountDict = []
        self.dbMng = db.ActTable()

    def add(self, account: Account):
        return self.dbMng.add_act(account)

    def dele(self, account):
        return self

    def update(self, account):
        return self

    def display(self, act_name):
        return self.account

    def display_all(self):
        act_all: dict = self.dbMng.get_act_all()
        print(act_all)
