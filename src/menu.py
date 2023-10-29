print('Tag! Wilkommen! \n German Vocab App \n')
menudict = {
    '1' : foodlist,
    '2' : spendinglist,
    '3' : timelist,
    '4' : travellist,
    '5' : healthlist,
    #'6' : peoplelist,
}
menuitem = input
def menu_start():
    input = input('INSTRUCTIONS: Choose a topic to generate a random list! \n 1. food \n 2. spending money \n 3. time \n 4. getting around \n 5. body and health \n')


    nav = input("Press 'f' to practice the list with flashcards \n Press 'm' to return to menu.")
        if nav ==  'm':
            print(menu_select)
        if nav == 'f':
        
        nav = input("Press 'q' for a quiz, \n 'l' to return to list, \n or 'm' to return to menu.")
        if nav == 'l':
            print(health_table)
        if nav == 'q':
            if nav == 'm':
                main.menu()
