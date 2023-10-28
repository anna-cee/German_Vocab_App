import csv
import random
import string
from prettytable import PrettyTable


table = PrettyTable()
germanlist = []
englishlist = []
contextlist = []

healthlist = open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')
spendinglist= open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig')
foodlist = open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig')
timelist = open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig')
travellist = open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig')

class randomList:
    def __init__(self, listname):
        self.vocablist = [r for r in csv.DictReader(listname)]
        self.randomlist = random.sample(self.vocablist, 10)
        #print(self.randomlist)
        for row in self.randomlist:
            for k, v in row.items():
                if k == "German":
                    germanlist.append(v)
            for k, v in row.items():
                if k == "English":
                    englishlist.append(v)
            for k, v in row.items():
                if k == "Context":
                    contextlist.append(v)
        table.add_column("German", germanlist)
        table.add_column("English", englishlist)
        table.add_column("Context", contextlist)
        print(table.get_string(fields=["German", "English"]))
       
        #for row in self.randomlist: 
            #print(f"{row['German']} : {row['English']}")
    

    # Setter
    # def set_list(self, listname):
    #     x.add_column("German", germanlist)
    #     x.add_column("English", englishlist)
    #     x.add_column("Context", contextlist)
    #     print(x.get_string(fields=["German", "English"]))

    
    # def list_cycle(self, filename):
    #     response = input(f"Press ENTER to cycle the list or 'f' to exit.")
    #     while response != 'f':
    #         for i in germanlist:
    #             x.add_row(i)
    #             print(x)
    #         # for row in self.randomlist: 
    #         #     if response != 'f':
    #         #         response = input(row['German'])
    #         #         response = input(row['English'])
    #         #     print('\n')

            
                
        # x.add_column("English", englishlist)
        # x.add_column("Context", contextlist)
        # print(x.get_string(fields=["German", "English"]))




    def quiz_generator(self, listname):
        correctcounter = 0
        for item in self.randomlist:
            targetvocab = item['German']
            definevocab = item['English']
            cleantarget = targetvocab.rstrip()
            cleandefine = definevocab.rstrip()
            
            answer = input(f'What is the German for {cleandefine}? ')
            if answer == cleantarget:
                correctcounter += 1
                print(f"Richtig! {cleandefine} is '{cleantarget}'\n")
            while answer != cleantarget:
                answer = input(f"Nochmal eingeben bitte! (try again or hit 'c' to check answer)  \n ")  
                if answer == 'c':
                    answer = cleantarget
                    print(f"{cleandefine} is '{cleantarget}'")
                elif answer == cleantarget:
                    correctcounter += 1
                    print(f"Richtig! {cleandefine} is '{cleantarget}' \n")
        print(f" Toll! You remembered {correctcounter} items! \n")




            


# for row in self.randomlist: 
#             print(f"{row['German']} : {row['English']}")
#         print('\n')            


