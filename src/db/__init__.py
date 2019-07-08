import json
import threading

from src.db.constants import FILE_DIR

R = threading.Lock()

def connect_r(data_name):
    with open(FILE_DIR + "/" + data_name, 'r') as amt_o:
        amt = json.load(amt_o)
        return amt


