def start():
    #INTRO
    name = input("What is your adventurer's name?\n")
    print('Greetings, ' + name + '. Its adventure time!' )
    print("You are a doctor and you suddenly you wake up in the hospital")
    print("after you stretch and stuff u recognized there is blood on the wall")
    print("you hear a loud scream of somebody dying in the back of the hall")
    print("you need a way to escape the building")
    print("CAn YoU FiNd A wAy OuT?!")
    return

def intro():
    escape = input('would you like to escape?\nyes/no\n')
    if escape == 'yes':
        print('you start walking out of your room')
        
    elif escape == 'no':
        print('cool your dead!')
        quit()
    else:
        print("i don't understand that")
        return

def part1():
    print('To your left, you see the killer with red eyes ready to chase you')
    print('To your right you see another path to your doom ')
    print('There is a big broken window infront of you')
    print('Behind you is the room you woke up in')

    answer = input('which direction are you taking? > \nLeft/right/forward/backwards\n')

    if 'Left' in answer:
        game_over('he grabs you by your throat and slices your stomach and your organs falls on the ground.')
    elif 'Right' in answer:
        print('you walk towards the next hall and u see more trails comming your way')
    elif 'Foward' in answer:
        game_over('you look outside of the window and you decide to jump of the window')
    else:
        game_over('You go back to sleep and you accepted your fate')
        return

def part2():
    print('to your left, you see a giant red door in flames')
    print('to your right, you see a long dark hallway')
    print('there is a big chest infront of you.')
    print('behind you is the killer.')

    answer = input('which direction are you taking? > \nLeft/right/forward/backwards\n')
    if 'Left' in answer:
        game_over('you walk towards the door and grab the doorknob, you open the door and you see everything is on fire, you decided to join and burn with it.')
    elif 'Right' in answer:
        print('You run towards the dark hallway further away from the killer.')
    elif 'Foward' in answer:
        game_over('u walk towards the chest and decided to open it, you open the chest and it ended up to be a boobytrap!')
    else:
        game_over('you walk towards the killer just to die in his hands')
        return

def part3():
    print("to your left, you see a bear who hasen't eaten in 10 years in your path")
    print('to your right, you see couple of scared nurses who need help')
    print('infront of you is a shining door')
    print('behind you is the killer but u found a gun laying around')

    answer = input('What direction do you move? \nLeft/right/forward/backwards\n')

    if 'Left' in answer:
        print("you walk past the bear's corpse and continue you're escape in hell")
    elif 'Right' in answer:
        game_over('you walk towards the scared nurses but it ended up to be the henchmen of the killer')
    elif 'Foward' in answer:
        game_over('you walk towards the door and ended up falling in a put full of needles')
    else:
        game_over('you walk towards the killer just to die in his hands')
        return

def part4():
    print('to your left is a simple door...')
    print('to your right is another human being crying for help')
    print('infront of you is a open window')
    print('behind you is the bloodthirsty killer')

    answer = input('What direction do you move? \nLeft/right/forward/backwards\n')
    
    if 'Left' in answer:
        game_over("you walk towards the door and look in the little peep hole while opening the door, the gun in the other side pull the trigger and shot your brains out")
    elif 'Right' in answer:
        game_over("The crazy doctor start laughing while looking at you, he grabs you and put you in his electric chair, he start laughing more and raise the electricity to the max ending up killing you")
    elif 'Foward' in answer:
        print('you jump out of the window and landed on a a glass surface, u broke your leg but you ae determined to move forward and escape')
    else:
        game_over('you walk towards the killer just to die in his hands')
        return
    
def final():
    print('to your left you see the big exit gate of the hospital')
    print('to your right you see another exit gate but a bit smaller')
    print("infront of you is a gun w a note saying 'this is an shotgun to kill the killer but! if u kill him u got everything backwards'")
    print('behind you is the angry killer licking the blood of his machete')

    answer = input('What direction do you move? \nLeft/right/forward/backwards\n')

    if 'Left' in answer:
        win()
    elif 'Right' in answer:
        game_over("you walk to the wat smaller exit gate, you open the door and the cardboard exit gate drop in your head, the killer is behind you and he finish you off")
    elif 'Foward' in answer:
        game_over('you grab the gun and aim it to the killer, u shoot the gun but the barrel was aimed toward you instead of the killer, killing u at the end')
    else:
        game_over('you are in so much pain and just stopped walking cus of your broken leg')
    return

def win():
    print('you finally escaped the hospital!\nyou stepped into your car and drove out of the hospital\n \nCongratz!\n')

def game_over(reason):
    print('\n' + reason)
    print('Game Over!')

    play_again()

def play_again():

    print('\nDo you want to play again? (yes or no)')

    answer = input('').lower()

    if 'yes' in answer:
        start()
    else:
        exit()

start()
intro()
part1()
part2()
part3()
part4()
final()