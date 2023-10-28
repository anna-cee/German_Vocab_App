import csv
import random
import string
from prettytable import PrettyTable

from cli_color_py import red, bright_yellow, green, blue, bold, magenta

#print(green("hello"))
#print(bold(red("world")))

#print(bright_yellow("background", bg=True))


table = PrettyTable()
flashcard = PrettyTable()
germanlist = []
englishlist = []
contextlist = []

healthlist = open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')
spendinglist= open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig')
foodlist = open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig')
timelist = open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig')
travellist = open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig')


class Randomlist:
    def __init__(self, listdir):
        self.vocablist = [r for r in csv.DictReader(listdir)]
        self.randomlist = random.sample(self.vocablist, 10)
        self.workinglist = self.randomlist
        #print(self.workinglist)
        #print(self.workinglist)
        #self.germanlist = []
        #self.englishlist = []
        #self.contextlist = []

        #
  

class TableGenerator:
    def __init__(self, tablevocab):
        self.tablevocab = tablevocab
        self.germanlist = germanlist
        self.englishlist = englishlist
        self.contextlist = contextlist    
        for row in self.tablevocab:
            for k, v in row.items():
                   if k == "German":
                    germanlist.append(v)
            for k, v in row.items():
                if k == "English":
                    englishlist.append(v)
            for k, v in row.items():
                if k == "Context":
                    contextlist.append(v)
        table.add_column("German", self.germanlist)
        table.add_column("English", self.englishlist)
        table.add_column("Context", self.contextlist)
        self.vocabtable = table.get_string(fields=["German", "English"])
        print(green(self.vocabtable))
        
class FlashcardGenerator:
    def __init__(self, tablename):
        self.tablename = tablename
        response = input(f"Press ENTER to cycle the list or 'f' to exit.")
        index = 0
        while response != 'f':
            response = input()
            print(magenta('\n=================='))
            print(bold(magenta(germanlist[index])))
            response = (input(englishlist[index]))
            index += 1
            if index == len(englishlist):
                check = input("\n Nochmal? Go again? any key or 'f' to end \n")
                if check != 'f':
                    index = 0
              
                




#     def quiz_generator(self, listname):
#         correctcounter = 0
#         for item in self.randomlist:
#             targetvocab = item['German']
#             definevocab = item['English']
#             cleantarget = targetvocab.rstrip()
#             cleandefine = definevocab.rstrip()
            
#             answer = input(f'What is the German for {cleandefine}? ')
#             if answer == cleantarget:
#                 correctcounter += 1
#                 print(green(f"Richtig! {cleandefine} is '{cleantarget}'\n"))
#             while answer != cleantarget:
#                 answer = input(f"Nochmal eingeben bitte! (try again or hit 'c' to check answer)  \n ")  
#                 if answer == 'c':
#                     answer = cleantarget
#                     print(green(f"{cleandefine} is '{cleantarget}'"))
#                 elif answer == cleantarget:
#                     correctcounter += 1
#                     print(green(f"Richtig! {cleandefine} is '{cleantarget}' \n"))
#         print(magenta(f" Toll! You remembered {correctcounter} items! \n"))




            


# # for row in self.randomlist: 
# #             print(f"{row['German']} : {row['English']}")
# #         print('\n')            


#         #for row in self.randomlist: 
#             #print(f"{row['German']} : {row['English']}")
    

#     # Setter
#     # def set_list(self, listname):
#     #     x.add_column("German", germanlist)
#     #     x.add_column("English", englishlist)
#     #     x.add_column("Context", contextlist)
#     #     print(x.get_string(fields=["German", "English"]))
