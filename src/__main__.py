# 程序启动界面
import threading
from sqlite3.dbapi2 import Time
from threading import Timer
from time import sleep

import schedule as schedule

from src import count_money
from src.account.account import Account
from src.account.manager import AccountMng


def showTitle():
    print()
    print("===========================")
    print("**** 请选择您要执行的操作 ****")
    print("**** 1.查看当前所有账户金额 ****")
    print("**** 2.拆分收入 ****")
    print("**** 3.新增账户信息 ****")
    print("**** 4.修改账户信息 ****")
    print("**** 5.删除账户信息 ****")


def start():
    showTitle()
    # 选择输入
    opr_num = int(input("请输入操作编号："))
    manager = AccountMng()

    ## 执行增删改查操作
    if opr_num == 1:
        print("查看当前所有账户信息，请稍等……")

        manager.display_all()
    elif opr_num == 2:
        print("拆分收入，请输入收入金额：")
        income = float(input())
        sp_income = manager.split_income(income)
        print(sp_income)
    elif opr_num == 3:
        print("输入账户信息")
        new_acct = manager.create()
        manager.add(new_acct)
        print("账户新增结束")
    elif opr_num == 4:
        print("修改账户信息，请输入账户名称：")
        acct_name = input()
    elif opr_num == 5:
        acct_name = input("请输入账户名称：1")
        del_acct = Account()
        del_acct.actName = acct_name
        acct_all = manager.dele(del_acct)
        print("删除成功")
        for act in acct_all.values():
            print(act)


if __name__ == "__main__":
    print("**** 欢迎光临个人理财计算器 ****")
    while True:
        start()


