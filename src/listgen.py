#select random list the given vocab

#get range of the list
#how are you going to access the list?

#random.sample(test_dict.items(), 1)
# import csv
# import random
# #x=0
# with open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"{row['German']} : {row['English']}")
##YAAAYYY my list generator is working

import csv
import random


# body_and_health = open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')
# spending_money = open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig')
# food = open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig')
# time = open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig')
# travel_and_directions = open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig')

#data = [r for r in csv.reader(open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))]
def listGenerator(topic_filename):

    vocablist = [r for r in csv.DictReader(topic_filename)]
    randomlist = random.sample(vocablist, 10)
    for row in randomlist: 
        print(f"{row['German']} : {row['English']}")



def listCycle():

    for row in randomlist:
        input(row['German'])
        input(row['English'])


        












#for row in randomlist:
    #print(f"{row['German']} : {row['English']}")
#for item in randomlist[0:12]:
    #print(f"{item['German']} : {item['English']}")


#list cycle learning
# for item in randomlist:
#     input(item['German'])
#     input(item['English'])



# #list matching activity
# for item in randomlist:
#     meaning = input(f"Enter definition for {item['German']} ")
#     while meaning != item['English']:
#         meaning = input(f"Nochmal! Enter definition for {item['German']} ") 
#     if meaning == item['English']:
#         correctcounter += 1
#     print(f"Yes! {item['German']} = {item['English']}   Wunderbar!")

# print(f"You remembered {correctcounter} items!")









# ['term3', 'def3']
    #print(reader)
    # for row in reader:
    #     #x += 1
    #     vocablist = (f"{row['German']} means {row['English']}")
    #     vocablist = [vocablist]
    #     print(vocablist)
        
        #if x > 9:
        #break
       
        #vocablist = [(f"{row['German']} : {row['English']}")]
        #vocablist = list(reader)
        
     

# import csv
# import random

# with open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig') as vocab:
#     reader = csv.DictReader(vocab)
#     #vocablist= list(reader)  
#     #print(vocablist)
#     for row in vocab:   
#         print(row['German'])

        #print(f"{row['German']} means {row['English']} and an example is {row['Context']}.")

        #print(f.random.sample(10)f"{row[0]} : {row[1]}")

#"{row['German']} means {row['English']} and an example is {row['Context']}."
#def travel():
    #for i in len(travel_and_distance.cs)
#get number of vocab

#display the list