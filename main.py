from utils import json_handler
from management import tab_handler

if __name__ == "__main__":
    # print(json_handler.read_json('./menu.json'))
    item = {'name': 'CHURROS DO M5', 'price': 5.0}
    print(json_handler.write_json('./managmento.json', item))

    # table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    # table_2 = [
    #   {"id": 10, "amount": 3},
    #   {"id": 20, "amount": 2},
    #   {"id": 21, "amount": 5},
    # ]

    # print(tab_handler.calculate_tab(table_1))
    # print(tab_handler.calculate_tab(table_2))
    ...
