# -*- coding: utf-8 -*-
class CalculateAmt(object):
    def calcAmt(self, income):
        self.gooseMoney = income * 0.5
        self.dreamMoney = income * 0.3
        self.pocketMoney = income * 0.2
        amtDict = {}
        amtDict['gooseMoney'] = self.gooseMoney
        amtDict['dreamMoney'] = self.dreamMoney
        amtDict['pocketMoney'] = self.pocketMoney
        self.amtDict = amtDict
        print("鹅的账户增加金额：", self.gooseMoney)
        print("梦想储蓄罐的账户增加金额：", self.dreamMoney)
        print("零花钱的账户增加金额：", self.pocketMoney)
