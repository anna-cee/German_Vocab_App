#Welcome to the App Menu
#List of 5 topics

#I want a nav feature whre I can move from feature to feature through the app 
#or at least return to the app menu to choose a new topic


from cli_color_py import red, yellow, green, blue, bold, magenta
import classlist
import quiz 

#Nav keys
# m == menu_select
# l == list
# f == flashcards
# q = quiz

print(yellow('Tag! Wilkommen!\n'))
print(red('German Vocab App \n'))


def menu():

    menu_option= input('Choose. \n 1. health and body \n 2. time \n 3. food \n 4. getting around \n 5. spending money \n')

    if menu_option == '1':
        health_list = classlist.Randomlist(open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')) 
        #print(healthlist.workinglist)
        health_vocab = health_list.workinglist
        #print(healthvocab)
        health_table = classlist.TableGenerator(health_vocab)
    
        health_flashcards = classlist.FlashcardGenerator(health_table)
        
        health_quiz = quiz.QuizGenerator(health_vocab)
    

    #print(healthtable.vocabtable)
    
    

    elif menu_option == '2':
        time_list = classlist.Randomlist(open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig'))
        #print(healthlist.workinglist)
        time_vocab = time_list.workinglist
        #print(healthvocab)
        time_table = classlist.TableGenerator(time_vocab)
        #print(healthtable.vocabtable)
        #time_flashcards = classlist.FlashcardGenerator(time_table)
        #time_quiz = quiz.QuizGenerator(time_vocab)
        time_contextquiz = quiz.ContextQuizGenerator(time_vocab)

    elif menu_option == '3':
        food_list = classlist.Randomlist(open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig'))
        #print(healthlist.workinglist)
        food_vocab = food_list.workinglist
        #print(healthvocab)
        food_table = classlist.TableGenerator(foodv_ocab)
        #go back to menu or make flashcards or quiz
        #print(healthtable.vocabtable)
        food_flashcards = classlist.FlashcardGenerator(food_table)
        #Go back to menu to list or quiz
        food_quiz = classlist.QuizGenerator(food_vocab)
        #Got back to menu to flashcards or list
    elif menu_option == '4':
        travel_list = classlist.Randomlist(open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))
        #print(healthlist.workinglist)
        travel_vocab = travel_list.workinglist
        #print(healthvocab)
        travel_table = classlist.TableGenerator(travel_vocab)
        #print(healthtable.vocabtable)
        travel_flashcards = classlist.FlashcardGenerator(travel_table)
        travel_quiz = classlist.QuizGenerator(travel_vocab)
    elif menu_option == '5':
        spending_list = classlist.Randomlist(open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig'))
        #print(healthlist.workinglist)
        spending_vocab = spending_list.workinglist
        #print(healthvocab)
        spending_table = classlist.TableGenerator(spending_vocab)
        #print(healthtable.vocabtable)
        spending_flashcards = classlist.FlashcardGenerator(spending_table)
        spending_quiz = classlist.QuizGenerator(spending_vocab)

menu()

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




