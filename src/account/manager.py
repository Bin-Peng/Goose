#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-02 00:49
# @Author  : Michael
# @File    : manager.py
# @Software: PyCharm
from src.account.account import Account
from src.db import db


class AccountMng:
    def __init__(self):
        self.accountDict = []
        self.dbMng = db.ActTable()

    def add(self, account: Account):
        return self.dbMng.add_act(account)

    def dele(self, account):
        return self.dbMng.dele_act(account.actName)

    def update(self, account):
        return self

    def display(self, act_name):
        return self.account

    def get_act_all(self):
        act_all = self.dbMng.get_act_all()
        return act_all

    def display_all(self):
        act_all: dict = self.dbMng.get_act_all()
        print(act_all)

    # TODO 1）拆分比例可配置
    # TODO 2）可按照当前根目录账户数进行比例分配
    def split_income(self, income: float):
        income_split = {}
        income_split["下金蛋的鹅"] = income * 0.5
        income_split["梦想储蓄罐"] = income * 0.3
        income_split["零花钱"] = income * 0.2
        return income_split
