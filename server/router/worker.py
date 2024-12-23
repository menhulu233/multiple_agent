from flask import Blueprint
from view.login import login, logout
bp = Blueprint('auth', __name__, url_prefix='/auth')

# 定义规则
rules = [
    {'rule': '/login', 'endpoint': 'login', 'methods': ['GET', 'POST'], 'view_func': login},
    {'rule': '/logout', 'endpoint': 'logout', 'methods': ['GET', 'POST'], 'view_func': logout},
]

for rule in rules:
    bp.add_url_rule(**rule)



