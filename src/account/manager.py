#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-02 00:49
# @Author  : Michael
# @File    : manager.py
# @Software: PyCharm
from account.account import Account
from db import db


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

    def display(self):
        return self.account
