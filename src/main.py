#Welcome to the App Menu

#Pick a list by topic

#To list of topics

#Choose a topic and random list is selected
#German only is displayed
#User inputs to See the translations
#User can opt to cycle through all vocab and translations
#User can opt for quiz - vocab displays

#Pick a random noun


print('Tag! Wilkommen! \n German Vocab App \n')
print('INSTRUCTIONS: Choose a topic to generate a random list! \n 1. time. \n 2.food. \n 3.money. \n 4.')

#functio

      
   

      




import classlist

body_and_health = open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')
spending_money = open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig')
food = open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig')
time = open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig')
travel_and_directions = open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig')


healthlist = classlist.randomList(body_and_health)
timelist = classlist.randomList(time)
foodlist = classlist.randomList(food)
travellist= classlist.randomList(travel_and_directions)
spendinglist = classlist.randomList(spending_money)


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

