# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def __str__(self):
        return f"Hello {self.name}, you are in the {self.current_room.name}. Also... {self.current_room.description} \n"

    def move(self, direction):
        if direction == 'n':
            if self.current_room.n_to == None:
                return print("Broooo, you can't go there")
            self.current_room = self.current_room.n_to
        elif direction == 's':
            if self.current_room.s_to == None:
                return print("Broooo, you can't go there")
            self.current_room = self.current_room.s_to
        elif direction == 'w':
            if self.current_room.w_to == None:
                return print("Broooo, you can't go there")
            self.current_room = self.current_room.w_to   
        elif direction == 'e':
            if self.current_room.e_to == None:
                return print("Broooo, you can't go there")
            self.current_room = self.current_room.e_to
          
        else:
            return print("Broooooo, that's not even a valid direction")
        return self.current_room

    def on_grab(self, item_name):
        item = self.current_room.find_item(item_name)
        if item is None:
            print("No item here bro")
        else:
            self.inventory.append(item)
            self.current_room.remove_item(item)
            print(f'You have picked up {item_name}')

    def on_drop(self, item_name):
        item = self.current_room.find_item(item_name)
        if item is None:
            print("No item here")
        else:
            self.remove_item(item)
            self.current_room.add_item(item)
            print(f'You have dropped {item_name}')

    def check_inventory(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None

    def remove_item(self, item):
        self.inventory.remove(item)

    def print_inventory(self):
        if len(self.inventory) == 0:
            print("No items in inventory brooo")
        else:
            print("Items:")
            for i in self.inventory:
                print(i.name)

