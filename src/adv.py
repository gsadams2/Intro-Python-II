from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# Link rooms together
room['outside'].n_to = room['foyer']

room['foyer'].add_item(Item('spectacles', 'these are glosses used to find hidden passages & items'))
room['foyer'].add_item(Item('heineken', 'drink a heineken for super strength'))

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']

room['overlook'].add_item(Item('cloak', 'makes you invisible'))

room['narrow'].w_to = room['foyer']

room['narrow'].add_item(Item('gun', 'use it to shoot your enemies'))

room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['treasure'].add_item(Item('phone', 'use the phone to call your mommy'))

# Main
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


bernard = Player("Bernard", room["outside"])

print(bernard)

command = input(' Move in a direction (N, S, E, W) or hit q to quit: \n')




directions = ['n', 's', 'e', 'w']



while not command == 'q':
    if any(i in command for i in directions):
        bernard.move(command)
        print(bernard)
        bernard.current_room.print_items()
        print("Do you wish to enter another room?")
        command = input(' Move in a direction (N, S, E, W) or hit q to quit: \n')
        split_command = command.split()
        if len(split_command) == 2:
            if split_command[0] == 'drop':
                bernard.on_drop(split_command[1])
            elif split_command[0] == 'grab':
                bernard.on_grab(split_command[1]) 
    elif command == "i":
        bernard.print_inventory()
        break
    else:
        print("invalid brooooo")
        print("Do you wish to enter another room?")
        
        
#Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
