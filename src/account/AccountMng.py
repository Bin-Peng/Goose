#账户管理类  账户的增删改查以及展示都应该通过该类
import src.db.db
from account.Account import Account


class AccountMng(object):
    def __init__(self):
        self.accountDict = []
        self.dbMng = src.db.db.Database()

    def add(self, account: Account):

        self.accountDict[account]

    def dele(self, account):
        self.account = account

    def update(self, account):
        self.account = account
        """
        展示所有账户信息
        """
    def display(self):
        dbMng
        return self.account
