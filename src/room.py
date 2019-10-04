# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)
    
    def print_items(self):
        if len(self.item_list) == 0:
            print('No items here, bro')
        else:
            for i in self.item_list:
                print(f'Items: {i.name}')

    def remove_item(self, item):
        self.item_list.remove(item)
    
    def find_item(self, item_name):
        for item in self.item_list:
            if item.name == item_name:
                return item
        return None


