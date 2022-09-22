import json


def read_json(path: str):
    try:
        with open(path, 'r', encoding='utf8') as file:
            items = json.load(file)
        if len(items) != 0:
            return items
        return []
    except:
        return []


def write_json(path: str, item: dict):
    items_list = read_json(path)
    with open(path, 'w', encoding='utf8') as file:
        if len(items_list) == 0:
            new_item = {
                'id': 1,
                'name': item['name'],
                'price': item['price'],
            }
            items_list.append(new_item)
            json.dump(items_list, file, indent=2)
            return item
        else:
            found = [
                items_in_list for items_in_list in items_list 
                if items_in_list['name'] == item['name']
            ]
            if len(found) != 0:
                answer = input('We already had an item with this name, want to proceed instead?(write Y or N)')
                if answer == 'Y':
                    ids = [
                        item_in_list['id'] for item_in_list in items_list
                    ]
                    generated_id = max(tuple(ids))
                    new_item = {
                        'id': generated_id + 1,
                        'name': item['name'],
                        'price': item['price'],
                    }
                    items_list.append(new_item)
                    json.dump(items_list, file, indent=2)
                    return new_item
                else:
                    json.dump(items_list, file, indent=2)
                    return 'Try register other item'
            else:
                ids = [
                    item_in_list['id'] for item_in_list in items_list
                    ]
                generated_id = max(tuple(ids))
                new_item = {
                'id': generated_id + 1,
                'name': item['name'],
                'price': item['price'],
            }
                items_list.append(new_item)
                json.dump(items_list, file, indent=2)
                return new_item
                    