from datetime import datetime
from utils import json_handler


STR_FORMATACAO = '%d/%m/%Y %H:%M:%S'

def calculate_tab(list: list[dict]):
    items_list = json_handler.read_json('menu.json')
    total_amount = 0
    for item in list:
        item_found = [item_list 
                        for item_list in items_list 
                        if item_list['id'] == item['id']
                        ]
        total_amount += (item_found[0]['price'] * item['amount'])
    data = datetime.now()
    return {'created_at': data.strftime(STR_FORMATACAO), 'subtotal': total_amount}


