import random
pranked = ['Rey', 'Ricky', 'Lukas', 'Simon', 'Adrian', 'Kevin', 'Dom', 'Jackie', 'Chris', 'Sayid']
room = ['Mos room', 'the cafeteria', 'the library', 'the main office', 'the bathroom']

def clue():
    victim = pranked[random.randrange(0,10)]
    location = room[random.randrange(0,5)]
    prank = pranked[random.randrange(0,10)]
    
    chance = random.randrange(0,100)
    if chance < 10:
        print(victim," got water ballooned in ", location," by ", prank)
    elif chance < 30:
        print(victim," got pied in the face in ", location," by ", prank)
    elif chance < 65:
        print(victim," got chocolate chip cookies that were actually oatmeal raisin in ", location," by ", prank)
    elif chance < 80:
        print(victim," got their shoelaces tied together in ", location," by ", prank)
    else:
        print(victim," got turned into a bunny with a transfiguration raygun in ", location," by ", prank)
        
clue()
