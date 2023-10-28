#Welcome to the App Menu
#List of 5 topics

#I want a nav feature whre I can move from feature to feature through the app 
#or at least return to the app menu to choose a new topic


from cli_color_py import red, yellow, green, blue, bold, magenta
import classlist

#Nav keys
# m == menu_select
# l == list
# f == flashcards
# q = quiz

print(yellow('Tag! Wilkommen!'))
print(red('German Vocab App \n'))

menu_select = input('Choose. \n 1. health and body \n 2. time \n 3. food \n 4. getting around \n 5. spending money \n')

if menu_select == '1':
    healthlist = classlist.Randomlist(open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')) 
    #print(healthlist.workinglist)
    healthvocab = healthlist.workinglist
    #print(healthvocab)
    healthtable = classlist.TableGenerator(healthvocab)
    nav = input("Press 'f' to practice the list with flashcards \n Press 'm' to return to menu.")
    if nav ==  'm':
        print(menu_select)
    if nav == 'f':
        healthflashcards = classlist.FlashcardGenerator(healthtable)
    nav = input("Press 'q' for a quiz, \n 'l' to return to list, \n or 'm' to return to menu.")
    if nav == 'l':
        print(healthtable)
    if nav == 'q':
        healthquiz = classlist.QuizGenerator(healthvocab)
    if nav == 'm':
        print(menu_select)


    #print(healthtable.vocabtable)
    
    

elif menu_select == '2':
    timelist = classlist.Randomlist(open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig'))
    #print(healthlist.workinglist)
    timevocab = timelist.workinglist
    #print(healthvocab)
    timetable = classlist.TableGenerator(timevocab)
    #print(healthtable.vocabtable)
    timeflashcards = classlist.FlashcardGenerator(timetable)
    healthquiz = classlist.QuizGenerator(timevocab)

elif menu_select == '3':
    foodlist = classlist.Randomlist(open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig'))
    #print(healthlist.workinglist)
    foodvocab = foodlist.workinglist
    #print(healthvocab)
    foodtable = classlist.TableGenerator(foodvocab)
    #go back to menu or make flashcards or quiz
    #print(healthtable.vocabtable)
    foodflashcards = classlist.FlashcardGenerator(foodtable)
    #Go back to menu to list or quiz
    foodquiz = classlist.QuizGenerator(foodvocab)
    #Got back to menu to flashcards or list
elif menu_select == '4':
    travellist = classlist.Randomlist(open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))
    #print(healthlist.workinglist)
    travelvocab = travellist.workinglist
    #print(healthvocab)
    traveltable = classlist.TableGenerator(travelvocab)
    #print(healthtable.vocabtable)
    travelflashcards = classlist.FlashcardGenerator(traveltable)
    travelquiz = classlist.QuizGenerator(travelvocab)
elif menu_select == '5':
    spendinglist = classlist.Randomlist(open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig'))
    #print(healthlist.workinglist)
    spendingvocab = spendinglist.workinglist
    #print(healthvocab)
    spendingtable = classlist.TableGenerator(spendingvocab)
    #print(healthtable.vocabtable)
    spendingflashcards = classlist.FlashcardGenerator(spendingtable)
    spendingquiz = classlist.QuizGenerator(spendingvocab)



# def navigate():
#     response = input("Press 'm' to return to menu or 'n' to go to next feature")
#     if response =='m':
#         print(menu_select)
#     if response =='n':
        
            



    
   

    


    #def set_list(menuitem):
    #     for num, listname in menudict.items():
    #         if menuitem == num:
    #            listname.set_list(listname)

    # set_list(menuitem)
    
  

    #     for num, filename in menudict.items():
    #         if menuitem == num:
    #             filename.set_list(filename)

    # listtable(menuitem)

    #navchoice = input('Enter = learn list or m = return to menu  ')
    #if navchoice == 'm':
        #main()


    # def cycle_loader(menuitem):
    #     for k, v in menudict.items():
    #         if menuitem == k:
    #             v.list_cycle(v)
    #             #listname = v

   # cycle_loader(menuitem)

    # navchoice = input('Enter = continue to quiz or m = return to menu  ')
    # if navchoice == 'm':
    #    # main()

    # def quiz_loader(menuitem):
    #     input('ENTER to start a recall quiz \n')
    #     for k, v in menudict.items():
    #         if menuitem == k:
    #             v.quiz_generator(v)
    #             #listname = v

    #quiz_loader(menuitem)




