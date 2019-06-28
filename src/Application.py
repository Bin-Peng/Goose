# 程序启动界面

print("**** 欢迎光临个人理财计算器 ****")
print("**** 请选择您要执行的操作 ****")
print("**** 1.查看当前所有账户金额 ****")
print("**** 2.拆分收入 ****")
print("**** 3.修改账户信息 ****")
# 选择输入
oprNum = int(input())
## 执行增删改查操作
if oprNum == 1:
    print("查看当前所有账户信息，请稍等……")
elif oprNum ==2:
    print("拆分收入，请输入收入金额：")
    income = float(input())
elif oprNum ==3:
    print("修改账户信息，请输入账户名称：")
    acctName = input()