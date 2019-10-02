# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def __str__(self):
        return f"Hello {self.name}, you are in the {self.current_room.name}. Also... {self.current_room.description} \n"

    def move(self, direction):
        if direction == 'n':
            if self.current_room.n_to == None:
                return print("Movement isn't allowed")
            self.current_room = self.current_room.n_to
        elif direction == 's':
            if self.current_room.s_to == None:
                return print("Movement isn't allowed")
            self.current_room = self.current_room.s_to
        elif direction == 'w':
            if self.current_room.w_to == None:
                return print("Movement isn't allowed")
            self.current_room = self.current_room.w_to   
        elif direction == 'e':
            if self.current_room.e_to == None:
                return print("Movement isn't allowed")
            self.current_room = self.current_room.e_to         
        else:
            return print("Invalid direction")
        return self.current_room



"""
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Hello {self.name}, you are {self.current_room.name}. Also... {self.current_room.description} \n"
    
    def move(self, direction):
        if direction == 'n':
            if self.current_room.n_to == None:
                return print("Yo, you can't go there")
            self.current_room == self.current_room.n_to
        elif direction == 'e':
            if self.current_room.e_to == None:
                return print("Yo, you can't go there")
            self.current_room == self.current_room.e_to
        elif direction == 's':
            if self.current_room.s_to == None:
                return print("Yo, you can't go there")
            self.current_room == self.current_room.s_to
        elif direction == 'w':
            if self.current_room.w_to == None:
                return print("Yo, you can't go there")
            self.current_room == self.current_room.w_to
        else: 
            return print("Brooooo, that's not a valid direction to go")
        return self.current_room
"""