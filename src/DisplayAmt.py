import json


def showAmt():
    with open('resource/Amt.json', 'r') as amt_j:
        amt = json.load(amt_j)
        amtSum = amt['gooseMoney'] + amt['dreamMoney'] + amt['pocketMoney']
        print('当前账户余额:', amt['gooseMoney'] + amt['dreamMoney'] + amt['pocketMoney'])
        print('鹅的账户金额' + str(amt['gooseMoney']) + '  占比：' + str(float(amt['gooseMoney']) / amtSum))
        print('梦想储蓄罐的账户增加金额：', str(amt['dreamMoney']) + '  占比：' + str(float(amt['dreamMoney']) / amtSum))
        print('零花钱的账户增加金额: ', str(amt['pocketMoney']) + '  占比：' + str(float(amt['pocketMoney']) / amtSum))


showAmt()
