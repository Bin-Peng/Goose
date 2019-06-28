#账户类  每个资金账户都应该以这个为单位
class Account:
    def __init__(self):
        # 账户名称
        self.actName = ""
        # 账户金额
        self.money = 0
        # 账户利率
        self.rates = 0
        # 账户利息
        self.ratesMoney = 0
        # 账户盈利
        self.income = 0
        # 子账户字典
        self.actSubAccount = []
