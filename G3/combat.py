def arena():
    print ('''welcome to the aren, we have many opponents for you to fight.
who would you like to fighh?
    1 - mouse
    2 - Rat
    3 - ROUS''')

    opponent_choice = str(input('please select your opponent: '))

    if (opponent_choice == '1'):
        opponent = 'mouse'
    elif (opponent_choice == '2'):
        print(dev.rat.name)
        opponent = rat
    elif (opponent_choice == '3'):
        opponent = ROUS

    print ("Your opponent is")
    print_status(opponent)
    print ("Your details are")
    print_status(user)
    combat_action(opponent)
