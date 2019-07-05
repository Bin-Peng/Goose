from concurrent.futures.thread import ThreadPoolExecutor

from account.account import Account
from account.manager import AccountMng

count_money_pool = ThreadPoolExecutor(max_workers=1)


def count_money():
    manager = AccountMng()
    act_all: dict = manager.get_act_all()
    acct_list: list[Account] = list(act_all.values())
    # while True:
    for act_dict in acct_list:  # type: Account
        act = Account(**act_dict)
        parent_act: Account = Account(**act_all[act.act_parent_name])
        sub_act_name_list: list = parent_act.act_sub_acct_name
        sub_act_name_list.append(act.actName)
        parent_act.act_sub_acct_name = set(sub_act_name_list)

        sub_acct_money = 0
        for sub_acct in act.act_sub_acct_name:
            sub_acct_money = sub_acct_money + act_all[sub_acct].money
        act.money = sub_acct_money
        act_all.setdefault(act.actName, act)


count_money_pool.submit(count_money(), "总金额计算")
