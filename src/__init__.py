import logging
import threading
from concurrent.futures.thread import ThreadPoolExecutor

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
    # print("后台计算金额")
    manager = AccountMng()
    sub_act_name_dict: dict = {}
    act_all: dict = manager.get_act_all()
    # 保存子账户集合
    for value in act_all.values():  # type: dict
        act_parent_name = value[ACT_PARENT_NAME]
        if act_parent_name not in sub_act_name_dict.keys():
            sub_act_name_dict.setdefault(act_parent_name, [value[ACT_NAME]])
        else:
            name = sub_act_name_dict[act_parent_name]
            name.append(value[ACT_NAME])
            update_dict = {act_parent_name: name}
            sub_act_name_dict.update(update_dict)

    # 更新act_all 并保存数据库
    sub_act_name_dict.pop("root")
    for key in sub_act_name_dict.keys():
        act_all[key][ACT_SUB_ACCT_NAME] = sub_act_name_dict[key]
    lock = manager.get_lock()
    lock.acquire()
    manager.set_act_all(act_all)
    lock.release()
    # 计算所有子账户资金
    for value in act_all.values():
        if value[ACT_SUB_ACCT_NAME] is not None:
            money = 0
            list = value[ACT_SUB_ACCT_NAME]

            for act_name in list:
                money = act_all[act_name][MONEY] + money
            if len(list):
                value[MONEY] = money
            act_all.update({value[ACT_NAME]: value})
    # 保存数据库
    lock.acquire()
    manager.set_act_all(act_all)
    lock.release()
    timer = threading.Timer(1, count_money)
    timer.start()


count_money()
