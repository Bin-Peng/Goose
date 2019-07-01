# 程序启动界面
from account.manager import AccountMng
from src.account.account import  Account


def start():
    print("**** 欢迎光临个人理财计算器 ****")

    print("**** 请选择您要执行的操作 ****")
    print("**** 1.查看当前所有账户金额 ****")
    print("**** 2.拆分收入 ****")
    print("**** 3.新增账户信息 ****")
    print("**** 4.修改账户信息 ****")
    # 选择输入
    opr_num = int(input("请输入："))
    manager = AccountMng()

    ## 执行增删改查操作

    if opr_num == 1:
        print("查看当前所有账户信息，请稍等……")
        manager.display()
    elif opr_num == 2:
        print("拆分收入，请输入收入金额：")
        income = float(input())
    elif opr_num == 3:
        print("输入账户信息")
        new_acct = Account()
        new_acct.actName = input("请输入账户名称：")
        new_acct.money = input("请输入账户余额：")
        manager.add(new_acct)
        print("账户新增完成")
    elif opr_num == 4:
        print("修改账户信息，请输入账户名称：")
        acct_name = input()


if __name__ == "__main__":
    start()
