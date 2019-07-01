# 账户类  每个资金账户都应该以这个为单位
from Goose.src.db import db


class Account(object):
    def __init__(self):
        # 账户名称
        self.actName = ""
        # 账户金额
        self.money: float = 0
        # 账户利率
        self.rates: float = 0
        # 账户利息
        self.ratesMoney: float = 0
        # 账户盈利
        self.income: float = 0
        # 子账户字典
        self.actSubAccount: dict = []


class AccountMng(object):
    def __init__(self):
        self.accountDict = []
        self.dbMng = db.ActTable()

    def add(self, account: Account):
        self.dbMng.
        self.accountDict[account]

    def dele(self, account):

        return self
    def update(self, account):
        return self

    def display(self):
        return self.account