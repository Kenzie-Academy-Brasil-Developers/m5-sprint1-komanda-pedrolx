from utils import json_handler

if __name__ == "__main__":
    # print(json_handler.read_json('./menu.json'))
    item = {'name': 'CHURROS DO M5', 'price': 5.0, 'id': 35}
    print(json_handler.write_json('./menu.json', item))
    ...
