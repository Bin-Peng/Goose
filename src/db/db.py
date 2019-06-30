#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-01 00:04
# @Author  : pengb
# @File    : db.py
# @Software: PyCharm
import json

from src.db.constants import FILE_DIR


class ActTable(object):
    def __int__(self):
        with open(FILE_DIR + "/Amt.json", 'r') as amt_o:
            self.amt = json.load(amt_o)
        with open(FILE_DIR+ "/AmtName.json", 'r') as name_j:
            self.amt_names:dict = json.load(name_j)
    def add_act_name(self, name):
        if self.amt_names.