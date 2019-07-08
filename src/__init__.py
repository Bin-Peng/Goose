from concurrent.futures.thread import ThreadPoolExecutor

from src.account.account import Account
from src.account.constants_act import MONEY, ACT_SUB_ACCT_NAME, ACT_NAME
from src.account.manager import AccountMng

count_money_pool = ThreadPoolExecutor(max_workers=1)


def count_money():
    manager = AccountMng()
    lock = manager.get_lock()
    lock.acquire()
    act_all: dict = manager.get_act_all()
    acct_list: list[Account] = list(act_all.values())
    for act_dict in acct_list:  # type: Account
        act = Account.create(**act_dict)
        if act.act_parent_name == "root":
            continue
        parent_act_dict = act_all[act.act_parent_name]
        parent_act: Account = Account.create(**parent_act_dict)
        sub_act_name_list: list = parent_act.act_sub_acct_name
        sub_act_name_list.append(act.actName)
        parent_act_dict[ACT_SUB_ACCT_NAME] = list(set(sub_act_name_list))
        update_parent_act_dict = {parent_act_dict[ACT_NAME]: parent_act_dict}
        act_all.update(update_parent_act_dict)
        sub_acct_money = 0
        for sub_acct in act.act_sub_acct_name:
            sub_acct_money = sub_acct_money + act_all[sub_acct][MONEY]
        act.money = sub_acct_money
        act_all.setdefault(act.actName, act)
    manager.set_act_all(act_all)
    lock.release()


count_money_pool.submit(count_money(), "总金额计算")
