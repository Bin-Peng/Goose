import re

GOOSE = "下金蛋的鹅"
DREAM_ACT = "梦想储蓄罐"
POCKET_ACT = "零花钱"
HOUSE_ACT = "生活花费"

FILE_DIR = 'resource'
# 特殊符号分隔符
ORDER_PATTERN = re.compile(r'\?|[-+]?[.\w]+$')
