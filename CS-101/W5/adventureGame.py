print('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?')
light = ''

while light.upper != ("MATCH" or "FLASHLIGHT"):
    light = input()
    action = ''
    end_game = ''

    if light.upper() == "MATCH":
        print('You pick up the match and strike it, and for an instant, the forest around you is illuminated.\
You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? [Type EXIT to quit]')
        
        while action.upper() != ('RUN' or 'HIDE'):
            action = input()
            
            if action.upper() == 'RUN':
                print('You are now running!')
            elif action.upper() == 'HIDE':
                print('You are now hidding')
            elif action.upper() == 'EXIT':
                end_game = 'EXIT'
                break
            else:
                print('please enter an option')

    elif light.upper() == "FLASHLIGHT":
        print('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.\
Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? [Type EXIT to quit]')  

        while action.upper() != ('FOLLOW' or 'LOOK'):
            action = input()
            
            if action.upper() == 'FOLLOW':
                print('You are now following the path!')
            elif action.upper() == 'LOOK':
                print('You are looking in the trees')
            elif action.upper() == 'EXIT':
                end_game = 'EXIT'
                break
            else:
                print('please enter an option')
    
    else:
        if light.upper() == 'EXIT' or end_game == 'EXIT':
            print()
        else:
            print('Please select an option MATCH or FLASHLIGHT [Type EXIT to quit]')\

    if light.upper() == 'EXIT' or end_game == 'EXIT':
            break

print('DONE')