#Welcome to the App Menu
#List of 5 topics

#got 5 csv files with data

# I want a function that can trn that data into a random list
#which I can get, it is a dicirtonary

#I want to turn that random list into a table I can print to the terminal

#I want to turn that same list into flashcard cycler

#I want to generate a quiz from that same list.

#I have the code for each feature, I'm just not sure how to tie it all together with the table 


from cli_color_py import red, yellow, green, blue, bold, magenta
import classlist

print(yellow('Tag! Wilkommen!'))
print(red('German Vocab App \n'))

menu_select = input('Choose. \n 1. health and body \n 2. time \n 3. food \n 4. getting around \n 5. spending money \n')

if menu_select == '1':
    healthlist = classlist.Randomlist(open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig'))
elif menu_select == '2':
    timelist = classlist.Randomlist(open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig'))
elif menu_select == '3':
    foodlist = classlist.Randomlist(open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig'))
elif menu_select == '4':
    travellist = classlist.Randomlist(open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))
elif menu_select == '5':
    spendinglist = classlist.Randomlist(open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig'))

#trying to get some functionality from main.

#print(healthlist.workinglist)
healthvocab= healthlist.workinglist
#print(healthvocab)
healthtable = classlist.TableGenerator(healthvocab)
#print(healthtable.vocabtable)
healthflashcards = classlist.FlashcardGenerator(healthtable)



#classlist.FlashcardGenerator(healthtable)



# for num, listname in menudict.items():
#     if menuitem == num:
#         print(classlist.Randomlist(listname))
    
    
                #v.set_list(v)              
   
#Check csv locations
#instances of Randonlists

    
    # workinglist = Randomlist.workinglist
    # print(workinglist)

    

    # workinglist = classlist.workinglist

#    set_table(workinglist)
    


    


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




#Generate a random list by topic

#timelist.set_list(timelist)
#foodlist.set_list(foodlist)
#travellist.set_list(travellist)
#spendinglist.set_list(spendinglist)
#healthlist.set_list(healthlist)

#Practice the list
#timelist.list_cycle(timelist)
#foodlist.list_cycle(foodlist)
#travellist.list_cycle(travellist)
#spendinglist.list_cycle(spendinglist)
#healthlist.list_cycle(healthlist)

#Quiz yourself
#timelist.quiz_generator(timelist)
#foodlist.quiz_generator(foodlist)
#travellist.quiz_generator(travellist)
#spendinglist.quiz_generator(spendinglist)
#healthlist.quiz_generator(healthlist)



#Instruction for quiz zou are asked for the german word for an English meaning form your list
#Answer the question with w German word from the list
#Remember to use german spelling and include articles for nouns
#You get a score for the words you remember, it doesn't matter how many tries before getting the word
#You can check with ´c´ to get the meaning, for words you don´t remember.


# healthlist = classlist.randomList(body_and_health)
# timelist = classlist.randomList(time)
# foodlist = classlist.randomList(food)
# travellist= classlist.randomList(travel_and_directions)
# spendinglist = classlist.randomList(spending_money)

