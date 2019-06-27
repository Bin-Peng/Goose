import sys


import json

from Goose.src import CalculateAmt


def showTitle():
    print("*****理财计算器*****")
    print("下金蛋的鹅:50%   梦想储蓄罐：30%    零花钱：20%")


configPath = 'resource'
showTitle()
income = float(input("请输入收入金额:"))
calcAmt = CalculateAmt.CalculateAmt()
calcAmt.calcAmt(income)
account_old = {}
with open(configPath + '/Amt.json', 'r') as account_j:
    account = json.load(account_j)
    account_old = account
    print("原账户金额为", account_old)
account_amt = {}
account_amt['gooseMoney'] = calcAmt.gooseMoney + account_old['gooseMoney']
account_amt['dreamMoney'] = calcAmt.dreamMoney + account_old['dreamMoney']
account_amt['pocketMoney'] = calcAmt.pocketMoney + account_old['pocketMoney']
with open(configPath + '/Amt.json', 'w') as account_w:
    json.dump(account_amt, account_w)
with open(configPath + '/Amt.json', 'r') as account_nj:
    account_n = json.load(account_nj)
    print("新账户金额为", account_n)
