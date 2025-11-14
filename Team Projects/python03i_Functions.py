#Adventure Game - Lillian Ring
def display_title():
    print('''
    ------ Abandoned House Adventure ------
    You are looking for an orange crystal-like ball
    and find yourself at this abandoned house in
    a forest. You tell yourself to immediately book
    it out of there once you get what you came for.
    ____________________________________________
''')
    

def display_location(location_name):
    """Display description of current location."""
    
    if location_name == 'start':
        print('''
    You are at your car, the house is to the north.
    ''')
        return
   
    match location_name:
        case 'outside_house':
            print('''
    It's the house. It looks like no one has been here recently.
    The door seems slightly ajar, could there be any animals inside?
    ''')
           
        
        case 'forest':
            print('''
    The place is surrounded by trees on both sides.
    The objective is to find that ball, not explore the vast forest.
    ''')
            
        
        case 'forest2':
            print('''
    More trees... Let's turn back and go find the ball.
    ''')
        
        case 'car':
            print('''
    It's where I came from... My car isn't going to last another
    two years, that's for sure...
    ''')
        
        case 'foyer':
            print('''
    Man.. This place is dusty.. Well it is an abandonded house after all.
    There's a room to the right that seems to be the right place.
    ''')
        
        case 'study':
            print('''
    This seems to be a study. The orb could be in that desk over there.

    Hint: use the 'take' command.
    ''')
        case 'return':
            print('''
    *The land around you turns into a maze and you end up back at the start*
    This seems to be what happens when you don't listen... But what would you know?
''')
        case 'end': print("")
        case _: print("I can't seem to go any further than this...")
    

def process_move(move, current_location):
    """Takes the player's move and current location, returns the new location."""
    new_location = current_location
    
    if move == 'help':
        print("""
    ---- List of commands ----
    Directional Movement:
    'north' - Forwards
    'east' - Right
    'south' - Backwards
    'west' - Left
    ___________________________
    Other:
    'take' - takes object
    'quit' - Quits the game
    ___________________________ 
""")
        return current_location
    #north
    if move == 'north':
        if current_location == 'start':
            new_location = 'outside_house'
        elif current_location == 'outside_house':
            new_location = 'foyer'
        elif current_location == 'foyer':
            new_location = '_'
        elif current_location == 'car':
            new_location = 'start'
        elif current_location == '_':
            new_location = 'return'
        elif current_location == 'return':
            new_location = 'start'
        else:
            print('ERROR TBA')
            new_location = '_'
    #south
    if move == 'south':
        if current_location == 'start':
            new_location = 'car'
        elif current_location == 'outside_house':
            new_location = 'start'
        elif current_location == 'car':
            new_location = '_'
        elif current_location == 'foyer':
            new_location = 'outside_house'
        elif current_location == '_':
            new_location = 'return'
        elif current_location == 'return':
            new_location = 'start'

        else:
            print('ERROR TBA')
            new_location = '_'

    #east
    if move == 'east':
        if current_location == 'start':
            new_location = 'forest'
        elif current_location == 'outside_house':
            new_location = 'forest'
        elif current_location == 'forest':
            new_location = 'forest2'
        elif current_location == 'foyer':
            new_location = 'study'
        elif current_location == 'forest2':
            new_location = 'start'
        elif current_location == '_':
            new_location = 'return'
        elif current_location == 'return':
            new_location = 'start'
        else:
            print('ERROR TBA')
            new_location = '_'
     #west
    if move == 'west':
        if current_location == 'start':
            new_location = 'forest'
        elif current_location == 'outside_house':
            new_location = 'forest2'
        elif current_location == 'forest':
            new_location = 'forest2'
        elif current_location == 'foyer':
            new_location = '_'
        elif current_location == 'forest2':
            new_location = 'start'
        elif current_location == '_':
            new_location = 'return'
        elif current_location == 'return':
            new_location = 'start'
        else:
            print('ERROR TBA')
            new_location = '_'

    if move == 'take' and current_location == 'study':
        new_location = 'end'
        inventory.append('orb')
    
    return new_location
    

def endGame():
    print('''
Finally found it.
________________________

The orb ended up being something called a 'Dragon Ball'.
There are four red stars in the middle of the ball.

You booked it out of there, not wanting to outstay your presence.
________________________________________________________

        ---- Congratulatons! You Finished theGame! ----
''')


def check_win_condition():
    """Check if player has won. Return True if won, False otherwise."""
    if 'orb' in inventory:
        return True  # Yes, the player has won
    return False # No, the player has not won

# Main program
display_title()
current_location = "start"
inventory = []
playing = True

while playing:
    
    #Display where the player is
    display_location(current_location)
    
    #Get the player's command
    move = input("Enter Command ('help' for command list): ").lower()

    #Process the command
    if move == 'quit':
        playing = False
    else:
        #Get the new location from function
        new_location = process_move(move, current_location)
        
        #Update the player's location for the next loop
        current_location = new_location

    if check_win_condition():
        endGame()
        playing = False

print(" Thanks for Playing! ")

