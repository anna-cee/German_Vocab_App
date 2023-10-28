#Welcome to the App Menu

#Pick a list by topic

#To list of topics

#Choose a topic and random list is selected
#German only is displayed
#User inputs to See the translations
#User can opt to cycle through all vocab and translations
#User can opt for quiz - vocab displays

#Pick a random noun


  


import classlist


#Check csv locations

healthlist = open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')
spendinglist= open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig')
foodlist = open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig')
timelist = open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig')
travellist = open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig')

#Get Started: Welcome and Topic Menu!

def main():
    print('Tag! Wilkommen! \n German Vocab App \n')
    print('You can choose topic below and get a random vocab list of 10 items. \n 1. health and body \n 2. time \n 3. food \n 4. getting around \n 5. spending money \n')
    menuitem = input('Enter the # for your chosen topic  ')
    print(menuitem)
    menudict = {
    '1' : healthlist,
    '2' : timelist,
    '3' : foodlist,
    '4' : travellist,
    '5' : spendinglist,
    # '1' : classlist.randomList(healthlist),
  

    }

    def listloader(menuitem):
        for num, listname in menudict.items():
            if menuitem == num:
                classlist.randomList(listname)
                #print(listname)
                #filename.set_list(randomlist)
                #filename.set_list(filename)
                #print(filename)
                #v.set_list(v)
                #listname = v           
    listloader(menuitem)

    # def set_table(menuitem):
    #     for num, filename in menudict.items():
    #         if menuitem == num:
    #             filename.set_table(filename)

    # set_table(menuitem)
    
  

    #     for num, filename in menudict.items():
    #         if menuitem == num:
    #             filename.set_list(filename)

    # listtable(menuitem)

    #navchoice = input('Enter = learn list or m = return to menu  ')
    #if navchoice == 'm':
        #main()


    def cycle_loader(menuitem):
        for k, v in menudict.items():
            if menuitem == k:
                v.list_cycle(v)
                #listname = v

   # cycle_loader(menuitem)

    # navchoice = input('Enter = continue to quiz or m = return to menu  ')
    # if navchoice == 'm':
    #    # main()

    def quiz_loader(menuitem):
        input('ENTER to start a recall quiz \n')
        for k, v in menudict.items():
            if menuitem == k:
                v.quiz_generator(v)
                #listname = v

    #quiz_loader(menuitem)


main()


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

