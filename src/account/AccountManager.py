#账户管理类  账户的增删改查以及展示都应该通过该类
class AccountManager:
    def __init__(self):
        self.accountDict = []
    def addAct(self, account):
        self.accountDict[account]

    def delAct(self, account):
        self.account = account

    def updateAct(self, account):
        self.account = account

    def displayAct(self):
        return self.account
