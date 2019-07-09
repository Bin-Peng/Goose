from concurrent.futures.thread import ThreadPoolExecutor

from src.account.account import Account
from src.account.constants_act import MONEY, ACT_SUB_ACCT_NAME, ACT_NAME, ACT_PARENT_NAME
from src.account.manager import AccountMng

count_money_pool = ThreadPoolExecutor(max_workers=1)

'''
后台计算子账户与金额变更
1）循环遍历所有账户，保存对应父账户名称
2）将保存下来的父账户所属集合，保存到数据库中
3）所有账户遍历子账户集合，将所有子账户金额相加得到账户金额
'''


def count_money():
    print("后台计算金额")
    manager = AccountMng()
    sub_act_name_dict: dict = {}
    old_sub_act = {}
    act_all: dict = manager.get_act_all()
    # 保存子账户集合
    for value in act_all.values():  # type: dict
        act_parent_name = value[ACT_PARENT_NAME]
        if act_parent_name not in sub_act_name_dict:
            sub_act_name_dict.setdefault(act_parent_name, [value[ACT_NAME]])
        else:
            name = sub_act_name_dict[act_parent_name]
            name.append(value[ACT_NAME])
            update_dict = {act_parent_name: name}
            sub_act_name_dict.update(update_dict)

    # lock = manager.get_lock()
    #
    # update_act_all = False
    #
    # acct_list: list[Account] = list(act_all.values())
    # for act_dict in acct_list:  # type: Account
    #     act = Account.create(**act_dict)
    #     if act.act_parent_name == "root":
    #         continue
    #     elif act.act_parent_name not in act_all.keys():
    #         continue
    #     parent_act_dict = act_all[act.act_parent_name]
    #     parent_act: Account = Account.create(**parent_act_dict)
    #
    #     # 父账户更新子账户字典
    #     if act.actName not in parent_act.act_sub_acct_name:
    #         update_act_all = True
    #         sub_act_name_dict: list = parent_act.act_sub_acct_name
    #         sub_act_name_dict.append(act.actName)
    #         parent_act_dict[ACT_SUB_ACCT_NAME] = list(set(sub_act_name_dict))
    #         old_sub_act[parent_act.actName] = sub_act_name_dict
    #         if old_money[act.actName] is None:
    #             old_money[act.actName] = -1
    #
    #     # 父账户更新总收入
    #     if act.money != old_money[act.actName]:
    #         update_act_all = True
    #         parent_money = parent_act.money + act.money
    #         parent_act_dict[MONEY] = parent_money
    #         old_money[parent_act.actName] = parent_money
    #         old_money[act.actName] = act.money
    #
    #     # 更新进总账户中
    #     if update_act_all:
    #         update_parent_act_dict = {parent_act_dict[ACT_NAME]: parent_act_dict}
    #         act_all.update(update_parent_act_dict)
    # if update_act_all:
    #     lock.acquire()
    #     manager.set_act_all(act_all)
    #     lock.release()
    #     update_act_all = False
