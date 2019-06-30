import json

import src.db.db


class ActTable(src.db.db.Database):
    def get_acts(self):
        with open('FILE_DIR/Amt.json', 'r') as amt_j:
            amt = json.load(amt_j)
            self.json_amt = json(amt)

    def add_act_name(self, name):
