# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-02 00:49
# @Author  : Michael
# @File    : manager.py
# @Software: PyCharm
# 账户类  每个资金账户都应该以这个为单位
from account import constants_act


class Account:
    def __init__(self):
        constants_act
        # 账户名称
        self.actName = ""
        # 账户盈利
        self.income: float = 0
        # 账户金额
        self.money: float = 0
        # 账户利率
        self.rates: float = 0
        # 账户利息
        self.ratesMoney: float = 0
        # 子账户字典
        self.act_sub_acct_name: list = {}
        # 父账户名称
        self.act_parent_name = ""

    @staticmethod
    def create(**entries):
        new_account = Account()
        new_account.__dict__.update(entries)
        return new_account
