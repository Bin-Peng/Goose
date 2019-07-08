from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep

from src.account.account import Account
from src.account.constants_act import MONEY, ACT_SUB_ACCT_NAME, ACT_NAME
from src.account.manager import AccountMng

count_money_pool = ThreadPoolExecutor(max_workers=1)


def count_money():
    manager = AccountMng()
    old_money: dict = {}
    old_sub_act = {}
    for value in manager.get_act_all().values():  # type: dict
        old_money.setdefault(value[ACT_NAME], value[MONEY])
        old_sub_act.setdefault(value[ACT_NAME], value[ACT_SUB_ACCT_NAME])
    lock = manager.get_lock()

    update_act_all = False
    while True:
        sleep(1)
        act_all: dict = manager.get_act_all()
        acct_list: list[Account] = list(act_all.values())
        for act_dict in acct_list:  # type: Account
            act = Account.create(**act_dict)
            if act.act_parent_name == "root":
                continue
            parent_act_dict = act_all[act.act_parent_name]
            parent_act: Account = Account.create(**parent_act_dict)
            # 父账户更新子账户字典

            if act.actName not in parent_act.act_sub_acct_name:
                update_act_all = True
                sub_act_name_list: list = parent_act.act_sub_acct_name
                sub_act_name_list.append(act.actName)
                parent_act_dict[ACT_SUB_ACCT_NAME] = list(set(sub_act_name_list))
                old_sub_act[parent_act.actName] = sub_act_name_list
                if old_money[act.actName] is None:
                    old_money[act.actName] = -1

            # 父账户更新总收入
            if act.money != old_money[act.actName]:
                update_act_all = True
                parent_money = parent_act.money + act.money
                parent_act_dict[MONEY] = parent_money
                old_money[parent_act.actName] = parent_money
                old_money[act.actName] = act.money

            # 更新进总账户中
            if update_act_all:
                update_parent_act_dict = {parent_act_dict[ACT_NAME]: parent_act_dict}
                act_all.update(update_parent_act_dict)
        if update_act_all:
            lock.acquire()
            manager.set_act_all(act_all)
            lock.release()
            update_act_all = False
